class PaletteOverflowError(Exception):
  def __init__(self, tile_y, tile_x):
    self.tile_y = tile_y
    self.tile_x = tile_x

  def __str__(self):
    return '@ tile (%dy,%dx)' % (self.tile_y, self.tile_x)


class ColorNotAllowedError(Exception):
  def __init__(self, pixel, tile_y, tile_x, y, x):
    self.pixel = pixel
    self.tile_y = tile_y
    self.tile_x = tile_x
    self.y = y
    self.x = x

  def __str__(self):
    return ('%x %x %x @ tile (%dy,%dx) and pixel (%dy,%dx)' %
            (self.pixel[0], self.pixel[1], self.pixel[2],
             self.tile_y, self.tile_x, self.y, self.x))


class TooManyPalettesError(Exception):
  def __init__(self, num):
    self.num = num

  def __str__(self):
    return '%d palettes > 4' % self.num
