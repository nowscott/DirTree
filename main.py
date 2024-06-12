import os

# 配置项
ignore_files = ['.env', 'tree.py', 'directory_tree.txt', '.DS_Store', '.env.local']  # 忽略的文件
ignore_dirs = ['.git', '__pycache__', 'node_modules', '.next']  # 忽略的文件夹
virtual_root = "Root"  # 根目录名称

def print_directory_tree(startpath, output_file):
    with open(output_file, 'w') as f:
        # 打印和写入虚拟根目录名称
        print(f'/{virtual_root}')
        f.write(f'/{virtual_root}\n')

        # 捕获和存储整个目录结构
        paths = {}
        for root, dirs, files in os.walk(startpath, topdown=True):
            # 过滤忽略的目录和文件
            dirs[:] = [d for d in dirs if d not in ignore_dirs]
            files = [file for file in files if file not in ignore_files]

            # 获取从虚拟根目录到当前目录的相对路径
            relative_path = os.path.relpath(root, startpath)
            if relative_path == '.':
                relative_path = ''
            
            paths[relative_path] = (dirs, files)
        
        # 打印目录结构
        def print_tree(current_path, depth=0):
            dirs, files = paths.get(current_path, ([], []))
            indent = '    ' * depth + '|-- '

            for dir in dirs:
                dir_line = f"{indent}/{dir}"
                print(dir_line)
                f.write(dir_line + '\n')
                print_tree(os.path.join(current_path, dir), depth + 1)
            
            for file in files:
                file_line = f"{indent}{file}"
                print(file_line)
                f.write(file_line + '\n')
        
        print_tree('')  # 从根开始打印

if __name__ == '__main__':
    # 设定起始目录为脚本所在目录
    start_dir = os.getcwd()
    output_filename = 'directory_tree.txt'
    # 执行目录树生成
    print_directory_tree(start_dir, output_filename)
    print(f"Directory tree has been saved to {output_filename}")
