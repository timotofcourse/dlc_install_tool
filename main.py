import shutil
import customtkinter
import CTkMessagebox
from pathlib import Path

install_tool = customtkinter.CTk()
install_tool.title('DLC Install Tool')
install_tool.geometry('500x300')
install_tool.resizable(False, False)

# Class to hold the tool state
class DLCInstaller:
    def __init__(self):
        self.game_executable = ''
        self.dlc_path = ''
        self.dlc_install_folder = ''
        self.dlc_name = ''

    # Functions to handle messageboxes
    def show_error(self, title, message):
        CTkMessagebox.CTkMessagebox(title=title, message=message, icon='cancel')

    def show_info(self, title, message):
        CTkMessagebox.CTkMessagebox(title=title, message=message)

    # Select executable and validate
    def select_game_executable(self):
        filename = customtkinter.filedialog.askopenfilename()
        if filename and filename.endswith('.exe'):
            self.game_executable = filename
            game_path_textbox.configure(text=self.game_executable)
            self.dlc_install_folder = str(Path(self.game_executable).parent / 'game')
        else:
            self.show_error('Not a Valid Executable File', 'Please select a valid game executable file.')

    # Select DLC file and validate
    def select_dlc_file(self):
        filename = customtkinter.filedialog.askopenfilename()
        if filename and filename.endswith('.rpa'):
            self.dlc_path = filename
            dlc_path_textbox.configure(text=self.dlc_path)
            self.dlc_name = Path(self.dlc_path).name
        else:
            self.show_error('Not a Valid DLC File', 'Please select a valid .rpa file.')

    # Validate and install the DLC file
    def validade_and_install_dlc(self):
        if self.game_executable and self.dlc_path:
            try:
                # Copy the DLC file to the game's DLC folder
                shutil.copyfile(self.dlc_path, Path(self.dlc_install_folder) / self.dlc_name)
                self.show_info('DLC Installed', 'DLC Installed Successfully!')
            except Exception as e:
                self.show_error('Error Installing DLC', f'Could not install this DLC pack: {e}')
        else:
            self.show_error('Missing File', 'Please select both the game executable and the DLC file.')

# Create installer instance
installer = DLCInstaller()

# GUI components
game_path_label = customtkinter.CTkLabel(install_tool, text='Game Executable: ')
game_path_label.pack(padx=5, pady=5)

game_path_textbox = customtkinter.CTkLabel(install_tool, text=installer.game_executable)
game_path_textbox.pack(padx=5, pady=5)

game_path_locator = customtkinter.CTkButton(install_tool, text='Select Game Executable', command=installer.select_game_executable)
game_path_locator.pack(padx=5, pady=5)

dlc_path_label = customtkinter.CTkLabel(install_tool, text='DLC Pack Path: ')
dlc_path_label.pack(padx=5, pady=5)

dlc_path_textbox = customtkinter.CTkLabel(install_tool, text=installer.dlc_path)
dlc_path_textbox.pack(padx=5, pady=5)

dlc_path_locator = customtkinter.CTkButton(install_tool, text='Select DLC Location', command=installer.select_dlc_file)
dlc_path_locator.pack(padx=5, pady=5)

install_button = customtkinter.CTkButton(install_tool, text='Install DLC', command=installer.validade_and_install_dlc)
install_button.pack(padx=5, pady=5)

if __name__ == '__main__':
    install_tool.mainloop()
