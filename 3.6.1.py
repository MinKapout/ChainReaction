import pygame, sys
from pygame.locals import *

def peutJouer(plateau=[[]]):
    for x in plateau:
        for y in x:
            if y == 0:
                return True
    return False


def alignement(joueur, plateau=[[]]):
    if alignementLignes(joueur, plateau):
        return True
    if alignementColonnes(joueur, plateau):
        return True
    if alignementDiagonales(joueur, plateau):
        return True
    return False


def alignementLignes(joueur, plateau=[[]]):
    for x in plateau:
        total = 0
        for y in x:
            if y == joueur:
                total += 1
            else:
                total = 0
        if total >= 3:
            return True
    return False


def alignementColonnes(joueur, plateau=[[]]):
    for i in range(len(plateau)):
        total = 0
        for j in range(len(plateau)):
            if plateau[j][i] == joueur:
                total += 1
            else:
                total = 0
        if total >= 3:
            return True
    return False


def alignementDiagonales(joueur, plateau=[[]]):
    total1 = 0
    total2 = 0
    for i in range(len(plateau)):
        if plateau[i][i] == joueur:
            total1 += 1
        else:
            total1 = 0

        if plateau[i][len(plateau)-1-i] == joueur:
            total2 += 1
        else:
            total2 = 0
    return total1 >= 3 or total2 >= 3


def recupererListeCases(plateauUI):
    taille = plateauUI.topright[0] - plateauUI.topleft[0]
    liste = []
    j = 0
    for x in range(plateauUI.topleft[0], plateauUI.topright[0], taille//3):
        i = 0
        for y in range(plateauUI.topleft[1], plateauUI.bottomleft[1], taille//3):
            liste.append((pygame.Rect(x, y,  taille//3, taille//3), i, j))
            i += 1
        j += 1
    return liste


def recupererCase(pos, cases):
    for x in cases:
        if x[0].topleft[0] <= pos[0] <= x[0].topright[0] and x[0].topleft[1] <= pos[1] <= x[0].bottomleft[1]:
            return x
    return None

def dessinerPion(joueur, surface, pos, cases, plateau):
    case = recupererCase(pos, cases)
    if case is not None and plateau[case[1]][case[2]] == 0:
        if joueur == 1:
            startPos = (case[0].topleft[0] + 20, case[0].topleft[1] + 20)
            endPos = (case[0].bottomright[0] - 20, case[0].bottomright[1] - 20)
            pygame.draw.line(surface, NOIR, startPos, endPos, 2)

            startPos = (case[0].topright[0] - 20, case[0].topright[1] + 20)
            endPos = (case[0].bottomleft[0] + 20, case[0].bottomleft[1] - 20)
            pygame.draw.line(surface, NOIR, startPos, endPos, 2)
        else:
            pygame.draw.circle(surface, NOIR, case[0].center, int((case[0].topright[0] - case[0].topleft[0])/2 - 20), 2)

        plateau[case[1]][case[2]] = joueur
        return True

    return False

def dessinerJeu(surface, l,h):
    surface.fill(NOIR)
    plateauTaille = h-200
    plateau = pygame.Rect(l/2 - (plateauTaille/2), h/2 - (plateauTaille/2), plateauTaille, plateauTaille)
    pygame.draw.rect(surface, BLEU, plateau)

    #Lignes verticales
    pygame.draw.line(surface, NOIR, (plateau.topleft[0] + plateauTaille/3, plateau.topleft[1]),
                     (plateau.topleft[0] + plateauTaille/3, plateau.bottomleft[1]), 2)
    pygame.draw.line(surface, NOIR, (plateau.topleft[0] + (plateauTaille / 3) * 2, plateau.topleft[1]),
                     (plateau.topleft[0] + (plateauTaille / 3) * 2, plateau.bottomleft[1]), 2)

    #Lignes horizontales
    pygame.draw.line(surface, NOIR, (plateau.topleft[0], plateau.topleft[1] + plateauTaille/3),
                     (plateau.topright[0], plateau.topleft[1] + plateauTaille / 3), 2)
    pygame.draw.line(surface, NOIR, (plateau.topleft[0], plateau.topleft[1] + (plateauTaille / 3) * 2),
                     (plateau.topright[0], plateau.topleft[1] + (plateauTaille / 3) * 2), 2)

    nouveauJeuBouton, nJRect = recupererTexte("Nouvelle partie")
    quitterBoutton, qRect = recupererTexte("Quitter")
    nJRect.topright = (l - h / 10, h / 10)
    qRect.topright = (nJRect.topright[0], nJRect.bottomleft[1] + 20)
    maSurface.blit(nouveauJeuBouton, nJRect)
    maSurface.blit(quitterBoutton, qRect)
    pygame.display.update()
    return plateau, nJRect, qRect

def recupererTexte(texte):
    fontObj = pygame.font.Font('freesansbold.ttf', 20)
    texteSurface = fontObj.render(texte, True, NOIR, BLEU)
    texteRect = texteSurface.get_rect()
    return texteSurface, texteRect



# === PROGRAMME PRINCIPAL ====
plateauDeJeu = [[0]*3 for i in range(3)]
pygame.init()
BLEU = (0, 0, 255)
NOIR = (0, 0, 0)
size = (1000, 700)
maSurface = pygame.display.set_mode(size)
pygame.display.set_caption('Morpion')
plateauUI, nJRect, qRect = dessinerJeu(maSurface, size[0], size[1])
cases = recupererListeCases(plateauUI)



joueur = 1
inProgress = True
mancheFini = False
while inProgress:
    for event in pygame.event.get():
        if event.type == QUIT:
            inProgress = False
        elif event.type == MOUSEBUTTONUP:
            if nJRect.topleft[0] <= event.pos[0] <= nJRect.topright[0] and nJRect.topleft[1] <= event.pos[1] <= nJRect.bottomleft[1]:
                plateauDeJeu = [[0] * 3 for i in range(3)]
                plateauUI, nJRect, qRect = dessinerJeu(maSurface, size[0], size[1])
                joueur = 1
                mancheFini = False
            elif qRect.topleft[0] <= event.pos[0] <= qRect.topright[0] and qRect.topleft[1] <= event.pos[1] <= qRect.bottomleft[1]:
                inProgress = False
            elif not mancheFini:
                aJoue = dessinerPion(joueur, maSurface, event.pos, cases, plateauDeJeu)

                if not aJoue:
                    continue

                mancheGagne = alignement(joueur, plateauDeJeu)

                if mancheGagne:
                    texteSurface, texteRect = None, None
                    texteSurface, texteRect = recupererTexte("Le joueur " + str(joueur) + " a gagné")
                    texteRect.topleft = (size[0] / 10, size[1] - (size[1] / 10))
                    maSurface.blit(texteSurface, texteRect)
                    mancheFini = True
                elif not peutJouer(plateauDeJeu):
                    texteSurface, texteRect = recupererTexte("Match nul")
                    texteRect.topleft = (size[0]/10, size[1] - (size[1] /10))
                    maSurface.blit(texteSurface, texteRect)
                    mancheFini = True

                joueur = 1 if joueur == 2 else 2
                pygame.display.update()
pygame.quit()
