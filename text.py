import hashlib
from collections import deque

# Lịch sử kết quả để cải thiện độ chính xác
history = deque(maxlen=1000)
correct_predictions = {"Tài": 0, "Xỉu": 0}

# Chuyển mã MD5 thành số nguyên
def md5_to_number(md5_hash: str) -> int:
    return int(md5_hash, 16)

# Xác định tài/xỉu từ MD5
def determine_result(md5_hash: str) -> str:
    number = md5_to_number(md5_hash)
    dice_rolls = [(number >> (i * 8)) % 6 + 1 for i in range(3)]
    dice_total = sum(dice_rolls)

    return "Tài" if dice_total >= 11 else "Xỉu"

# Ghi nhận kết quả đúng sai
def update_accuracy(predicted: str, actual: str):
    if predicted == actual:
        correct_predictions[predicted] += 1
    history.append((predicted, actual))

# Giao diện chính
def main():
    print("🔰tool free by @tranphattx🔰")
    print("📌địt mẹ mày tao làm free đừng mang đi  bán 25 nghìn nhé🤣")
    while True:
        md5_hash = input("👉 Nhập mã MD5 để phân tích: ").strip()

        if md5_hash.lower() == "exit":
            print("🚪 Thoát tool. Hẹn gặp lại!")
            break

        if len(md5_hash) != 32 or not all(c in "0123456789abcdefABCDEF" for c in md5_hash):
            print("⚠️ Mã MD5 không hợp lệ! Hãy nhập lại.")
            continue

        predicted_result = determine_result(md5_hash)
        print(f"💵 Dự đoán: {predicted_result}")

        actual_result = input("✅ Kết quả thực tế (Tài/Xỉu): ").strip().capitalize()
        if actual_result in ["Tài", "Xỉu"]:
            update_accuracy(predicted_result, actual_result)

if __name__ == "__main__":
    main()
