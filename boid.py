from pygame import Vector2, draw, display, time
import utils
import math

screen = display.set_mode((1280, 1280))
clock = time.Clock()

class Boid:
    def __init__(self, x, y, vx, vy, r, color):
        self.position = Vector2(x, y)
        self.velocity = Vector2(vx, vy)
        self.r = r
        self.color = color
        self.size = self.r * 2.5
        

    def update(self, boids):
        if int(self.position.x) in range(200, utils.screen_width - 200) and int(self.position.y) in range(200, utils.screen_height - 200):
            self.velocity += self.cohesion(boids) * utils.centering_factor

        self.velocity += self.alignment(boids) * utils.matching_factor
        self.velocity += self.separation(boids) * utils.avoid_factor

        self.edges()

        speed = math.sqrt(self.velocity.x**2 + self.velocity.y**2)
        if speed > utils.max_speed:
            self.velocity.x = (self.velocity.x/speed) * utils.max_speed
            self.velocity.y =(self.velocity.y/speed) * utils.max_speed

        if speed < utils.min_speed:
            self.velocity.x = (self.velocity.x/speed) * utils.min_speed
            self.velocity.y = (self.velocity.y/speed) * utils.min_speed

        self.position += self.velocity


    def separation(self, boids):
        """
        Boids move away from other boids too close to them
        """
        close = Vector2(0, 0)

        for b in boids:
            if b == self:
                continue
        
            if self.position.distance_to(b.position) < utils.protected_range:
                close += self.position - b.position

        return close
    
    
    def alignment(self, boids):
        """
        Boids match the velocity of their neighbors
        """
        avg_vel = Vector2(0, 0)
        neighboring_boids = 0

        for b in boids:
            if b == self:
                continue
    
            if self.position.distance_to(b.position) < utils.visible_range:
                avg_vel += b.velocity
                neighboring_boids += 1

        avg_vel = avg_vel/neighboring_boids if neighboring_boids else avg_vel
        return avg_vel
    

    def cohesion(self, boids):
        """
        Boids fly towards the centre of mass of neighbouring boids
        centre of mass = average position of all the boids in the visible range
        """
        avg_pos = Vector2(0, 0)
        neighboring_boids = 0

        for b in boids:
            if b == self:
                continue
        
            if self.position.distance_to(b.position) < utils.visible_range:
                avg_pos += b.position
                neighboring_boids += 1

        avg_pos = avg_pos/neighboring_boids if neighboring_boids else avg_pos
        return avg_pos


    def edges(self):
        if self.position.x > utils.screen_width - self.size:
            self.velocity.x -= utils.turn_factor

        elif self.position.x < self.size:
            self.velocity.x += utils.turn_factor

        if self.position.y > utils.screen_height - self.size:
            self.velocity.y -= utils.turn_factor

        elif self.position.y < self.size:
            self.velocity.y += utils.turn_factor


    def draw(self):
        angle = math.atan2(self.velocity.y, self.velocity.x)
        point1 = self.position + Vector2(math.cos(angle), math.sin(angle)) * self.size
        point2 = self.position + Vector2(math.cos(angle + 2.5), math.sin(angle + 2.5)) * self.size
        point3 = self.position + Vector2(math.cos(angle - 2.5), math.sin(angle - 2.5)) * self.size

        draw.polygon(screen, self.color, [point1, point2, point3])
        '''
        # boid tail
        tail_length = 25
        trailing_point = self.position - Vector2(math.cos(angle), math.sin(angle)) * tail_length
        draw.line(screen, self.color, self.position, trailing_point, 1)
        '''