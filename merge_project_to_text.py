import os

# CẤU HÌNH
PROJECT_PATH = r'D:\Tests\source-code\selenium-python\ui-test'  # Thay đổi đường dẫn đến folder dự án của bạn
OUTPUT_FILE = 'Selenium_Project_Source_Full.txt'
EXCLUDED_DIRS = {'.git', '.idea', '__pycache__', 'venv', 'env', '.pytest_cache'} # Các folder cần bỏ qua

def merge_project_to_text(root_dir, output_file):
    with open(output_file, 'w', encoding='utf-8') as outfile:
        # Ghi phần mở đầu để NotebookLM hiểu ngữ cảnh
        outfile.write(f"DOCUMENTATION FOR PROJECT: {os.path.basename(root_dir)}\n")
        outfile.write("="*50 + "\n\n")

        for root, dirs, files in os.walk(root_dir):
            # Lọc bỏ các thư mục không cần thiết
            dirs[:] = [d for d in dirs if d not in EXCLUDED_DIRS]
            
            for file in files:
                if file.endswith('.py'): # Chỉ lấy file Python (hoặc thêm .json, .yaml nếu cần)
                    file_path = os.path.join(root, file)
                    # Tạo đường dẫn tương đối để AI hiểu cấu trúc thư mục
                    relative_path = os.path.relpath(file_path, root_dir)
                    
                    try:
                        with open(file_path, 'r', encoding='utf-8') as infile:
                            content = infile.read()
                            
                            # ĐÁNH DẤU RÕ RÀNG TÊN FILE (Rất quan trọng để AI định vị code)
                            outfile.write(f"\n{'='*20} START OF FILE: {relative_path} {'='*20}\n")
                            outfile.write(content)
                            outfile.write(f"\n{'='*20} END OF FILE: {relative_path} {'='*20}\n\n")
                            
                        print(f"Đã thêm: {relative_path}")
                    except Exception as e:
                        print(f"Lỗi đọc file {relative_path}: {e}")

    print(f"\nĐã hoàn tất! File kết quả: {output_file}")

# Chạy hàm
if __name__ == "__main__":
    merge_project_to_text(PROJECT_PATH, OUTPUT_FILE)