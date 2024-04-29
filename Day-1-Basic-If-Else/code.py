def calculate_can_chi_calender(year):
    result = ""
    can = ["Canh", "Tân", "Nhâm", "Quý", "Giáp", "Ất", "Bính", "Đinh", "Mậu", "Kỉ"]

    chi = [
        "Thân",
        "Dậu",
        "Tuất",
        "Hợi",
        "Tí",
        "Sửu",
        "Dần",
        "Mẹo",
        "Thìn",
        "Tị",
        "Ngọ",
        "Mùi",
    ]

    for i in range(len(can)):
        for j in range(len(chi)):
            if year % 10 == i and year % 12 == j:
                result = can[i] + " " + chi[j]

    return result


def main():
    print(
        f"Test case 1: calculate_can_chi_calender(2024): {calculate_can_chi_calender(2024)}"
    )
    print(
        f"Test case 2: calculate_can_chi_calender(2023): {calculate_can_chi_calender(2023)}"
    )
    print(
        f"Test case 3: calculate_can_chi_calender(1997): {calculate_can_chi_calender(1997)}"
    )


if __name__ == "__main__":
    main()
