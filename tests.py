import simple_choices


def test_choice():
    class Fruit(simple_choices.SimpleChoice):
        orange = 'It is an orange'
        apple = 'Green apple'

    assert Fruit.apple == 'apple'
    assert Fruit.orange == 'orange'

    expected_choice = (
        ('orange', 'It is an orange'),
        ('apple', 'Green apple'),
    )

    assert Fruit.choices == expected_choice
