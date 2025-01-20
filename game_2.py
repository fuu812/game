import pygame as pg
import time

scale_factor = 3  # 画像のスケールファクター
chip_s = 24  # ウィンドウの大きさを変えないために元のサイズを使用
hito_1 = pg.image.load('./data/noboru.png')
hito_2 = pg.image.load('./data/noboru2.png')

# 画像をスケーリングする
hito_1 = pg.transform.scale(
    hito_1, (hito_1.get_width() * scale_factor, hito_1.get_height() * scale_factor))
hito_2 = pg.transform.scale(
    hito_2, (hito_2.get_width() * scale_factor, hito_2.get_height() * scale_factor))

class PlayerCharacter:

  def __init__(self, init_pos, img_path):
    self.pos = pg.Vector2(init_pos)
    self.size = pg.Vector2(24, 32) * scale_factor
    self.dir = 2

def main():

  pg.init()
  pg.display.set_caption('クモイトダッシュ！')
  map_s = pg.Vector2(16, 9)
  disp_w = int(chip_s * map_s.x * 2)
  disp_h = int(chip_s * map_s.y * 2)
  screen = pg.display.set_mode((disp_w, disp_h))
  clock = pg.time.Clock()
  font = pg.font.Font(None, 15)
  large_font = pg.font.Font(None, 72)  # 大きなフォントサイズを設定
  exit_flag = False
  exit_code = '000'
  hito_now = hito_1

  pushcount = 0
  hito = PlayerCharacter((3, 6), hito_now)

  # カウントダウン
  for i in range(3, 0, -1):
    screen.fill(pg.Color('BLACK'))
    countdown_text = large_font.render(f'{i}', True, 'WHITE')
    countdown_rect = countdown_text.get_rect(
        center=(disp_w // 2, disp_h // 2))
    screen.blit(countdown_text, countdown_rect)
    pg.display.update()
    time.sleep(1)

  start_time = time.time()

  while not exit_flag:

    cmd_move = -1
    for event in pg.event.get():
      if event.type == pg.QUIT:
        exit_flag = True
        exit_code = '001'

      if event.type == pg.KEYDOWN:
        pushcount += 1
        if event.key == pg.K_SPACE:
          cmd_move = 0
          if hito_now == hito_1:
            hito_now = hito_2
          else:
            hito_now = hito_1

    screen.fill(pg.Color('BLACK'))

    # 画面の中央に縦方向の白い棒を描写
    line_width = 9  # 棒の太さを指定
    pg.draw.line(screen, 'WHITE', (disp_w // 2, 0),
                 (disp_w // 2, disp_h), line_width)

    # 画像を画面の中央に配置
    image_rect = hito_now.get_rect(center=(disp_w // 2, disp_h // 2))
    screen.blit(hito_now, image_rect.topleft)

    # pushcountに応じてウィンドウの下部を赤色にする
    if pushcount <= 5:
      pg.draw.rect(screen, 'RED', (0, disp_h *
                   3 // 4, disp_w, disp_h // 4))
    elif pushcount <= 10:
      pg.draw.rect(screen, 'RED', (0, disp_h *
                   4 // 5, disp_w, disp_h // 5))
    elif pushcount <= 15:
      pg.draw.rect(screen, 'RED', (0, disp_h *
                   9 // 10, disp_w, disp_h // 10))
    elif pushcount <= 20:
      pg.draw.rect(screen, 'RED', (0, disp_h *
                   14 // 15, disp_w, disp_h // 15))

    # pushcountに応じてウィンドウの上部を水色にする
    if pushcount >= 30:
      pg.draw.rect(screen, 'CYAN', (0, 0, disp_w, disp_h // 15))
    if pushcount >= 35:
      pg.draw.rect(screen, 'CYAN', (0, 0, disp_w, disp_h // 10))
    if pushcount >= 40:
      pg.draw.rect(screen, 'CYAN', (0, 0, disp_w, disp_h // 5))
    if pushcount >= 45:
      pg.draw.rect(screen, 'CYAN', (0, 0, disp_w, disp_h // 4))

    # screen.blit(font.render(f'{pushcount}', True, 'WHITE'), (10, 20))

    elapsed_time = time.time() - start_time
    if elapsed_time >= 10:
      exit_flag = True
      if pushcount > 45:
        result_text = "game clear!"
      else:
        result_text = "game over..."
      result_surface = large_font.render(result_text, True, 'WHITE')
      result_rect = result_surface.get_rect(
          center=(disp_w // 2, disp_h // 2 + 50))
      screen.blit(result_surface, result_rect)
      pg.display.update()
      time.sleep(3)

    pg.display.update()
    clock.tick(30)

  pg.quit()
  return exit_code

if __name__ == "__main__":
  code = main()
  print(f"プログラムを「コード{code}」で終了しました。")
