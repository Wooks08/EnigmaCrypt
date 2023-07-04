class File_Manage:

    def read_file(self, fp):
        with open(fp, 'r') as f:
            file_lines = f.readlines()
            return file_lines

    def write_file(self, fp, file_lines):
        with open(fp, 'w') as f:
            f.writelines(file_lines)


file_manage = File_Manage()
file_manage.read_file('test.txt')
