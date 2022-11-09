import pygame
import constants

selectedCountry = None


def getTriangleArea(p1, p2, p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3

    return abs((x1 * (y2 - y3) + x2 * (y3 - y1)
                + x3 * (y1 - y2)) / 2.0)


class Country:
    selected = False
    coords = []
    name = ""
    player = ""

    def __init__(self, name, points, player):
        self.coords = points
        self.name = name
        self.player = player

    def draw(self, surface):
      if self.player == "p1":
        colour = pygame.Color("0xb51818") if self.selected else "red"
      elif self.player == "p2":
        colour = pygame.Color("0x014080") if self.selected else pygame.Color("0x0271ad")
        
      pygame.draw.polygon(
            surface, colour, self.coords, width=6 if self.selected else 4)

    def check(self, mouseCoord):
        global selectedCountry
        if len(self.coords) == 3:
            baseArea = getTriangleArea(
                self.coords[0], self.coords[1], self.coords[2])

            area1 = getTriangleArea(mouseCoord, self.coords[0], self.coords[1])
            area2 = getTriangleArea(mouseCoord, self.coords[1], self.coords[2])
            area3 = getTriangleArea(mouseCoord, self.coords[2], self.coords[0])
            checkArea = area1 + area2 + area3

            if baseArea == checkArea:
                selectedCountry = self
                self.selected = True

        elif len(self.coords) == 4:
            if mouseCoord[0] > self.coords[0][0] and mouseCoord[0] < self.coords[3][0] and mouseCoord[1] < self.coords[0][1] and mouseCoord[1] > self.coords[1][1]:
                selectedCountry = self
                self.selected = True

    # def attack():
        #use def checkGameBoard to check if country is next to it and then fill the country if troop count > than the other country?
        #use lists for each country to see if they can attack it
