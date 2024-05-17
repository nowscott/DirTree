
# Directory Tree Generator

## 介绍
这是一个Python脚本，用于生成指定目录的树形结构并保存到文件中。你可以配置需要忽略的文件和文件夹，以及根目录的名称。

## 功能
- 生成指定目录的树形结构
- 忽略特定的文件和文件夹
- 将目录树保存到一个文本文件中

## 配置
在脚本开头，你可以配置以下内容：
- `ignore_files`: 忽略的文件列表
- `ignore_dirs`: 忽略的文件夹列表
- `virtual_root`: 根目录的名称

## 使用方法
1. 克隆仓库到本地：
    ```sh
    git clone https://github.com/nowscott/dir_tree.git
    cd dir_tree
    ```

2. 运行脚本：
    ```sh
    python main.py
    ```

3. 生成的目录树将会保存到当前目录下的 `directory_tree.txt` 文件中。

## 示例
假设你有如下目录结构：
```
project/
    ├── .git/
    ├── .env
    ├── src/
    │   ├── main.py
    │   ├── utils.py
    ├── tree.py
    └── README.md
```

运行脚本后，生成的 `directory_tree.txt` 文件内容如下：
```
Root/
|-- src/
|   |-- main.py
|   |-- utils.py
|-- README.md
```

## 配置项说明
- `ignore_files`: 列表中的文件将被忽略，不会出现在生成的目录树中。例如，`.env`、`tree.py`、`directory_tree.txt` 等。
- `ignore_dirs`: 列表中的文件夹将被忽略，包括其子文件夹和文件。例如，`.git`、`__pycache__`、`node_modules`、`.next` 等。
- `virtual_root`: 指定生成目录树的根目录名称。

## 贡献
欢迎贡献代码！请 fork 本仓库并提交 PR。

## 许可证
该项目采用 [MIT 许可证](LICENSE)。
