# В данном коде все прокомментировано как надо,
# но слишком избыточно.
# Избавьтесь от комментариев, изменив имена переменных, 
# чтобы было понятно, за что эти переменные отвечают 
# и что происходит и без комментариев


class Unit:

    def move(self, field, x_coord, y_coord, direction, fly, crawl, base_speed: int = 1):

        if fly and crawl:
            raise ValueError('Рожденный ползать летать не должен!')

        if fly:
            base_speed *= 1.2
            if direction == 'UP':
                new_y = y_coord + base_speed
                new_x = x_coord
            elif direction == 'DOWN':
                new_y = y_coord - base_speed
                new_x = x_coord
            elif direction == 'LEFT':
                new_y = y_coord
                new_x = x_coord - base_speed
            elif direction == 'RIGHT':
                new_y = y_coord
                new_x = x_coord + base_speed
        if crawl:
            base_speed *= 0.5
            if direction == 'UP':
                new_y = y_coord + base_speed
                new_x = x_coord
            elif direction == 'DOWN':
                new_y = y_coord - base_speed
                new_x = x_coord
            elif direction == 'LEFT':
                new_y = y_coord
                new_x = x_coord - base_speed
            elif direction == 'RIGHT':
                new_y = y_coord
                new_x = x_coord + base_speed

            field.set_unit(x=new_x, y=new_y, unit=self)


