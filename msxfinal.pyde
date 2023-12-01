

left = False

sledX = -100  # X-coordinate of the sled
numSnowflakes = 40
snowflakes = [None] * numSnowflakes  # Declare the array

num_humans = 10
human_radius = 15
speed_y = 1

def setup():
    size(600, 600)
    background(0)
    smooth(255)
    noStroke()
    global sledX, human_positions, speed_y, left
    human_positions = [random(height - 2 * human_radius) + human_radius for _ in range(num_humans)]
    sledX = -100  # Initial position of the sled outside the screen

    # Loop through array to create each snowflake object
    for i in range(len(snowflakes)):
        snowflakes[i] = Snowflake()  # Create each snowflake object

def draw():
    global sledX, human_positions, speed_y, left
    background(0,0,67)  # Background color
    fill(0, 0, 255)
    rect(300, 100, 100, 50)
    fill(255, 255, 255)
    rect(300, 50, 100, 50)
    fill(255, 0, 0)
    rect(300, 0, 100, 50)
    
    for i in range(num_humans):
        # Draw each human figure (circle)
        
        
        fill(242, 167, 124)
        ellipse((i + 1) * width / (num_humans + 1), human_positions[i] * 1.5 - 35, human_radius * 2, human_radius * 2)
        ellipse((i + 1) * width / (num_humans + 1) + 18, human_positions[i] * 1.5 - 8 , human_radius * 1.5, human_radius * 1.5)
        ellipse((i + 1) * width / (num_humans + 1) - 18, human_positions[i] * 1.5 - 4 , human_radius * 1.5, human_radius * 1.5)
        ellipse((i + 1) * width / (num_humans + 1) + 9, human_positions[i] * 1.5 + 23 , human_radius * 1.5, human_radius * 2)
        ellipse((i + 1) * width / (num_humans + 1) - 9, human_positions[i] * 1.5 + 21 , human_radius * 1.5, human_radius * 2)
        fill(65, 232, 93)  # Set the fill color to skin colour
        ellipse((i + 1) * width / (num_humans + 1), human_positions[i] * 1.5 , human_radius * 2.3, human_radius * 2.7)
        
        # Update the position of each human figure (make them bounce)
        human_positions[i] += speed_y  # Adjust the bouncing speed
        
        # Check if a human figure has reached the bottom or the top
        if human_positions[i] > height - human_radius or human_positions[i] < human_radius:
            speed_y = -speed_y  # Reverse the direction for all human figures

    # Move the sled to the right
    if sledX == 0:
        left = False
    if sledX == 500:
        left = True
        
    if left == True:
        sledX -= 2
    else:
        sledX += 2
    
        
    
        
                # if sledX != 500:
    #     sledX += 2  # Change this value to adjust speed

    # Draw sled
    fill(139, 69, 19)  # Brown color for sled
    rect(sledX, height - 50, 100, 20)  # Sled base
    rect(sledX + 40, height - 70, 20, 20)  # Sled front

    # Santa
    fill(255, 224, 189)  # Skin color
    ellipse(sledX + 50, height - 90, 40, 40)  # Head
    fill(255, 0, 0)  # Red hat
    triangle(sledX + 30, height - 100, sledX + 70, height - 100, sledX + 50, height - 130)  # Hat base
    fill(255)  # White pom-pom
    ellipse(sledX + 50, height - 130, 15, 15)  # Pom-pom
    fill(0)  # Black eyes
    ellipse(sledX + 40, height - 90, 10, 10)  # Left eye
    ellipse(sledX + 60, height - 90, 10, 10)  # Right eye
    noFill()
    stroke(0)
    arc(sledX + 50, height - 80, 30, 20, 0, PI)  # Smile

    # Loop through array to update and display snowflakes
    for i in range(len(snowflakes)):
        snowflakes[i].fall()

class Snowflake:
    def __init__(self):
        self.x = random(width)
        self.y = random(-height)
        self.size = random(5, 10)

    def fall(self):
        self.y += 3
        fill(255)
        ellipse(self.x, self.y, self.size, self.size)

        if self.y > height:
            self.x = random(width)
            self.y = random(-200)
