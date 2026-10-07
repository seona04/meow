from pico2d import *

# 1st commit: initialize canvas and load resource images
TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

tuk_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
speed = 5
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

    x += (int(SDLK_RIGHT in pressed_keys) - int(SDLK_LEFT in pressed_keys)) * speed
    y += (int(SDLK_UP in pressed_keys) - int(SDLK_DOWN in pressed_keys)) * speed

    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    character.clip_draw(0, 300, 100, 100, x, y)
    update_canvas()
    delay(0.05)

close_canvas()
