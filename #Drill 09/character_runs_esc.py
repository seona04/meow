from pico2d import *

# 1st commit: initialize canvas and load resource images
TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

tuk_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
speed = 5
frame = 0
facing_right = True
pressed_keys = set()


def handle_events():
    global running

    for event in get_events():
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False
            elif event.key in (SDLK_UP, SDLK_DOWN, SDLK_LEFT, SDLK_RIGHT):
                pressed_keys.add(event.key)
        elif event.type == SDL_KEYUP:
            pressed_keys.discard(event.key)


while running:
    handle_events()

    if SDLK_RIGHT in pressed_keys:
        facing_right = True
    elif SDLK_LEFT in pressed_keys:
        facing_right = False

    dx = int(SDLK_RIGHT in pressed_keys) - int(SDLK_LEFT in pressed_keys)
    dy = int(SDLK_UP in pressed_keys) - int(SDLK_DOWN in pressed_keys)
    x += dx * speed
    y += dy * speed

    moving = dx != 0 or dy != 0
    if moving:
        animation_y = 100 if facing_right else 0
    else:
        animation_y = 300 if facing_right else 200

    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    character.clip_draw(frame * 100, animation_y, 100, 100, x, y)
    update_canvas()
    frame = (frame + 1) % 8
    delay(0.05)

close_canvas()
