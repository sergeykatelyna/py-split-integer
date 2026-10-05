from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert (
        sum(split_integer(17, 4)) == 17
    ), "Sum of the parts should be equal to 8"


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert (
        len(set(split_integer(6, 2))) == 1
    ), "Number of the parts should be even if the value is divisible by parts"


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert (
        split_integer(8, 1) == [8]
    ), "The part should be equal to [8] if split into one part"


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert (
        split_integer(32, 6) == sorted(split_integer(32, 6))
    ), "The parts should be sorted if they are not equal"


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert (
        split_integer(3, 6).count(0) == 3
    ), "Some parts should be zero if value is less than number of parts"


def test_part_should_differ_by_one() -> None:
    assert (
        max(split_integer(32, 7)) - min(split_integer(32, 7)) <= 1
    ), "The parts should be sorted if they are not equal"
