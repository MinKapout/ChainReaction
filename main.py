import pygame, sys
from pygame.locals import *


def newBoard(n,m):
    gameBoard = [[[0,0] for x in range(n)] for y in range(m)]
    return gameBoard

def possible(gameBoard,n,m,i,j,player):
    if i in range(n) and j in range(m):
        if player == gameBoard[i][j][0] or gameBoard[i][j][0] == 0:
            return True
        else:
            return False
    else:
        return False

def put(gameBoard,n,m,i,j,player):
    gameBoard[i][j][0] = player
    gameBoard[i][j][1] += 1
    if (i == 0 or i == n-1) and (j == 0 or j == m-1):
        if gameBoard[i][j][1]== 2:
            if i == 0:
                put(gameBoard,n,m,i+1,j,player)
            else:
                put(gameBoard,n,m,i-1,j,player)
            if j ==0:
                put(gameBoard,n,m,i,j+1,player)
            else:
                put(gameBoard,n,m,i,j-1,player)
    elif i == 0 or i == n-1:
        if gameBoard[i][j][1]==3:
            if i ==0:
                put(gameBoard, n, m, i, j - 1, player)
                put(gameBoard, n, m, i, j + 1, player)
                put(gameBoard, n, m, i + 1, j, player)
            else:
                put(gameBoard, n, m, i, j - 1, player)
                put(gameBoard, n, m, i, j + 1, player)
                put(gameBoard, n, m, i - 1, j, player)
    elif j == 0 or j == m-1:
        if gameBoard[i][j][1] == 3:
            if j ==0:
                put(gameBoard, n, m, i + 1, j, player)
                put(gameBoard, n, m, i - 1, j, player)
                put(gameBoard, n, m, i, j + 1, player)
            else:
                put(gameBoard, n, m, i + 1, j, player)
                put(gameBoard, n, m, i - 1, j, player)
                put(gameBoard, n, m, i, j - 1, player)
    else:
        if gameBoard[i][j][1] == 4:
            put(gameBoard, n, m, i + 1, j, player)
            put(gameBoard, n, m, i - 1, j, player)
            put(gameBoard, n, m, i, j + 1, player)
            put(gameBoard, n, m, i, j - 1, player)

def loose(gameBoard,n,m,player):
    playerLoose == []
    for i in range(0,n-1):
        for j in range(0,m-1):
            if gameBoard[i][j][1] != 0 :
                return False

    playerLoose.append(player)
    return True

def win(gameBoard,n,m,player):
    for x in range(0,player+1):
        if len(player_loose) == x-1:
            return True
        else:
            return False




def initGame(mySurface):
    mySurface.fill(NOIR)
    plateau = pygame.Rect(l / 2 - (plateauTaille / 2), h / 2 - (plateauTaille / 2), plateauTaille, plateauTaille)
    pygame.draw.rect(surface, BLEU, plateau)