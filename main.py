import pygame
import time

from constants import *
from game_board import *

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Project Hazard")
selectedCountry = None
selectedCountryName = "None"
playerTurn = "p1"
gamePhase =  "DRAFT"
running = True
confirm = False
confirm2 = False

while running:
  screen.fill((255, 99, 51))
  # Add main game board
  gameBoard = makeGameBoard("All")
  screen.blit(gameBoard, (0,0))

  # Selected text
  font = pygame.font.SysFont('arial', 30)
  selectedCountryText = font.render(
      "Selected: " + selectedCountryName, True, "black")
  selectedCountryRect = selectedCountryText.get_rect()
  selectedCountryRect.center = (380, 560)

  # Player turn text
  font = pygame.font.SysFont('arial', 21)
  playerTurnText = font.render(
      "Player Turn: " + playerTurn[-1], True, "black")
  playerTurnRect = playerTurnText.get_rect()
  playerTurnRect.center = (727, 10)

  # Game phase text
  gamePhaseText = font.render(
      gamePhase, True, "black")
  gamePhaseRect = gamePhaseText.get_rect()
  gamePhaseRect.center = (727, 50)

  # Confirm Text
  confirmText = font.render(
      "2nd Confirm?" if confirm2 else "Confirm?" if confirm else "", True, "black")
  confirmRect = confirmText.get_rect()
  confirmRect.center = (727, 90)

  screen.blit(selectedCountryText, selectedCountryRect)
  screen.blit(playerTurnText, playerTurnRect)
  screen.blit(confirmText, confirmRect)
  screen.blit(gamePhaseText, gamePhaseRect)

  for event in pygame.event.get():
      if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
          mouseX, mouseY = pygame.mouse.get_pos()

          selectedCountry = checkGameBoard(
              "All", (mouseX, mouseY), playerTurn)
          
          if selectedCountry != None:
            selectedCountryName = selectedCountry.name + " (" + str(country.selectedCountry.troops) + ")"
            confirm = True
          else:
            selectedCountryName = "None"
            confirm = False
      
      elif event.type == pygame.QUIT:
          running = False
          break
      
      
      elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:

        # For DRAFT Phase
        if gamePhase == "DRAFT" and selectedCountry != None:
          selectedCountry.troops += 2
          selectedCountryName = selectedCountry.name + " (" + str(country.selectedCountry.troops) + ")"
          
          gamePhase = "FORTIFY"
          selectedCountryName = "None"
          confirm = False
          checkGameBoard("All", (0, 0), playerTurn)
          
        elif gamePhase == "FORTIFY" and selectedCountry != None and confirm2 == False:
          confirm2 = True
          baseCountry = selectedCountry

          checkGameBoard("All", (0, 0), playerTurn)
          selectedCountry = None
          selectedCountryName = "None"
          confirm = False

        elif gamePhase == "FORTIFY" and selectedCountry != None and confirm2 and selectedCountry != baseCountry and selectedCountry.name in baseCountry.neighbours:
          confirm2 = False
          foritfy(baseCountry, selectedCountry)

          checkGameBoard("All", (0, 0), playerTurn)
          selectedCountry = None
          selectedCountryName = "None"
          confirm = False

          gamePhase = "DRAFT"
          playerTurn = "p1" if playerTurn == "p2" else "p2"
          
        
  pygame.display.update()