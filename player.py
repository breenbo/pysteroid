import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_SPEED, PLAYER_TURN_SPEED, SHOT_RADIUS, SHOT_SPEED


class Player(CircleShape):
    def __init__(self, x: float, y: float):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation: float = 0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right

        return [a, b, c]


    def draw(self, screen):
        color = "white"
        _ = pygame.draw.polygon(screen, color, self.triangle(), 2)


    def rotate(self, dt: float):
        self.rotation += PLAYER_TURN_SPEED * dt


    def move(self, dt: float):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt


    def update(self, dt: float):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_f]:
            self.rotate(dt)

        if keys[pygame.K_q]:
            self.rotate(-dt)

        if keys[pygame.K_s]:
            self.move(dt)

        if keys[pygame.K_d]:
            self.move(-dt)
            
        if keys[pygame.K_SPACE]:
            self.shoot()

    def shoot(self):
        shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
        shot.velocity = pygame.Vector2(0,1).rotate(self.rotation)
        shot.velocity *= SHOT_SPEED






class Shot(CircleShape):
    def __init__(self, x: float, y: float, radius: float):
        super().__init__(x, y, radius)

    def draw(self, screen):
        _ = pygame.draw.circle(screen, "red", self.position,  self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt



