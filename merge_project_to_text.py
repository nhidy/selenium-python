import os

# CẤU HÌNH
PROJECT_PATH = r'D:\Tests\source-code\selenium-python\ui-test' # Thay đường dẫn dự án của bạn
OUTPUT_PREFIX = 'merged\Source_Part'
MAX_FILE_SIZE_MB = 0.4  # Giới hạn mỗi file khoảng 0.5 MB (an toàn cho NotebookLM)
EXCLUDED_DIRS = {'.git', '.idea', '__pycache__', 'venv', 'env', '.pytest_cache', 'reports', 'logs', 'backup'}
ALLOWED_EXTENSIONS = {'.py', '.ini', '.yaml', '.json', '.sql', '.txt'} # Chỉ lấy các file code cần thiết

def split_project_to_text(root_dir, output_prefix, max_size_mb):
    max_bytes = max_size_mb * 1024 * 1024
    part_num = 1
    current_content = []
    current_size = 0

    def save_part(content_list, part_n):
        filename = f"{output_prefix}_{part_n:02d}.txt"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f"DOCUMENTATION PART {part_n}\n")
            f.write("="*50 + "\n\n")
            f.write("".join(content_list))
        print(f"-> Đã tạo: {filename} ({os.path.getsize(filename)/1024:.2f} KB)")

    for root, dirs, files in os.walk(root_dir):
        dirs[:] = [d for d in dirs if d not in EXCLUDED_DIRS]
        
        for file in files:
            ext = os.path.splitext(file)[1].lower()
            if ext in ALLOWED_EXTENSIONS:
                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(file_path, root_dir)
                
                try:
                    # Đọc nội dung file
                    with open(file_path, 'r', encoding='utf-8') as infile:
                        file_content = infile.read()
                        
                    # Tạo header cho file code đó
                    formatted_chunk = (
                        f"\n{'='*20} START OF FILE: {relative_path} {'='*20}\n"
                        f"{file_content}"
                        f"\n{'='*20} END OF FILE: {relative_path} {'='*20}\n\n"
                    )
                    
                    chunk_size = len(formatted_chunk.encode('utf-8'))

                    # Kiểm tra nếu cộng thêm file này thì có quá giới hạn không
                    if current_size + chunk_size > max_bytes:
                        # Lưu file hiện tại
                        save_part(current_content, part_num)
                        # Reset cho file mới
                        part_num += 1
                        current_content = []
                        current_size = 0
                    
                    current_content.append(formatted_chunk)
                    current_size += chunk_size
                    
                except Exception as e:
                    print(f"Bỏ qua file {relative_path}: {e}")

    # Lưu phần còn dư cuối cùng
    if current_content:
        save_part(current_content, part_num)

    print("\nHoàn tất! Hãy upload tất cả các file .txt vừa tạo lên NotebookLM.")

if __name__ == "__main__":
    split_project_to_text(PROJECT_PATH, OUTPUT_PREFIX, MAX_FILE_SIZE_MB)