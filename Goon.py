import socket
import threading
import time
from datetime import datetime
import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class SimpleTimeApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Network Time Server & Client")
        self.geometry("860x580")
        self.minsize(800, 520)

        self.server_socket = None
        self.server_running = False
        self.server_thread = None

        self.setup_ui()

    def setup_ui(self):
        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure(1, weight=1)

        header = ctk.CTkLabel(
            self,
            text="TCP Network Time Protocol",
            font=ctk.CTkFont(size=20, weight="bold")
        )
        header.grid(row=0, column=0, columnspan=2, padx=20, pady=(20, 10), sticky="w")

        self.build_server_frame()
        self.build_client_frame()

    def build_server_frame(self):
        frame = ctk.CTkFrame(self, corner_radius=10)
        frame.grid(row=1, column=0, padx=(20, 10), pady=(0, 20), sticky="nsew")
        frame.grid_columnconfigure(1, weight=1)
        frame.grid_rowconfigure(4, weight=1)

        title = ctk.CTkLabel(frame, text="Server", font=ctk.CTkFont(size=16, weight="bold"))
        title.grid(row=0, column=0, columnspan=2, padx=15, pady=(15, 10), sticky="w")

        ctk.CTkLabel(frame, text="Host:").grid(row=1, column=0, padx=(15, 5), pady=5, sticky="w")
        self.srv_host = ctk.CTkEntry(frame)
        self.srv_host.insert(0, "127.0.0.1")
        self.srv_host.grid(row=1, column=1, padx=(0, 15), pady=5, sticky="ew")

        ctk.CTkLabel(frame, text="Port:").grid(row=2, column=0, padx=(15, 5), pady=5, sticky="w")
        self.srv_port = ctk.CTkEntry(frame)
        self.srv_port.insert(0, "8888")
        self.srv_port.grid(row=2, column=1, padx=(0, 15), pady=5, sticky="ew")

        self.srv_btn = ctk.CTkButton(
            frame,
            text="Start Server",
            fg_color="#16a34a",
            hover_color="#15803d",
            command=self.toggle_server
        )
        self.srv_btn.grid(row=3, column=0, columnspan=2, padx=15, pady=10, sticky="ew")

        self.srv_log = ctk.CTkTextbox(frame, font=ctk.CTkFont(family="Consolas", size=12))
        self.srv_log.grid(row=4, column=0, columnspan=2, padx=15, pady=(0, 15), sticky="nsew")

    def build_client_frame(self):
        frame = ctk.CTkFrame(self, corner_radius=10)
        frame.grid(row=1, column=1, padx=(10, 20), pady=(0, 20), sticky="nsew")
        frame.grid_columnconfigure(1, weight=1)
        frame.grid_rowconfigure(5, weight=1)

        title = ctk.CTkLabel(frame, text="Client", font=ctk.CTkFont(size=16, weight="bold"))
        title.grid(row=0, column=0, columnspan=2, padx=15, pady=(15, 10), sticky="w")

        ctk.CTkLabel(frame, text="Host:").grid(row=1, column=0, padx=(15, 5), pady=5, sticky="w")
        self.cli_host = ctk.CTkEntry(frame)
        self.cli_host.insert(0, "127.0.0.1")
        self.cli_host.grid(row=1, column=1, padx=(0, 15), pady=5, sticky="ew")

        ctk.CTkLabel(frame, text="Port:").grid(row=2, column=0, padx=(15, 5), pady=5, sticky="w")
        self.cli_port = ctk.CTkEntry(frame)
        self.cli_port.insert(0, "8888")
        self.cli_port.grid(row=2, column=1, padx=(0, 15), pady=5, sticky="ew")

        self.cli_btn = ctk.CTkButton(frame, text="Request Time", command=self.request_time)
        self.cli_btn.grid(row=3, column=0, columnspan=2, padx=15, pady=10, sticky="ew")

        result_box = ctk.CTkFrame(frame, fg_color="#18181b")
        result_box.grid(row=4, column=0, columnspan=2, padx=15, pady=(0, 10), sticky="ew")

        self.time_label = ctk.CTkLabel(
            result_box,
            text="--:--:--",
            font=ctk.CTkFont(family="Consolas", size=16, weight="bold")
        )
        self.time_label.pack(pady=(8, 2))

        self.rtt_label = ctk.CTkLabel(result_box, text="Delay: -- ms", text_color="gray")
        self.rtt_label.pack(pady=(0, 8))

        self.cli_log = ctk.CTkTextbox(frame, font=ctk.CTkFont(family="Consolas", size=12))
        self.cli_log.grid(row=5, column=0, columnspan=2, padx=15, pady=(0, 15), sticky="nsew")

    def log_srv(self, text):
        stamp = datetime.now().strftime("%H:%M:%S")
        self.srv_log.insert("end", f"[{stamp}] {text}\n")
        self.srv_log.see("end")

    def log_cli(self, text):
        stamp = datetime.now().strftime("%H:%M:%S")
        self.cli_log.insert("end", f"[{stamp}] {text}\n")
        self.cli_log.see("end")

    def toggle_server(self):
        if not self.server_running:
            self.start_server()
        else:
            self.stop_server()

    def start_server(self):
        host = self.srv_host.get().strip()
        try:
            port = int(self.srv_port.get().strip())
        except ValueError:
            self.log_srv("Invalid port number.")
            return

        try:
            self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.server_socket.bind((host, port))
            self.server_socket.listen(5)
            self.server_running = True

            self.srv_btn.configure(text="Stop Server", fg_color="#dc2626", hover_color="#b91c1c")
            self.srv_host.configure(state="disabled")
            self.srv_port.configure(state="disabled")

            self.log_srv(f"Server started on {host}:{port}")

            self.server_thread = threading.Thread(target=self.accept_clients, daemon=True)
            self.server_thread.start()
        except Exception as e:
            self.log_srv(f"Error: {e}")
            if self.server_socket:
                self.server_socket.close()
            self.server_running = False

    def accept_clients(self):
        while self.server_running:
            try:
                self.server_socket.settimeout(1.0)
                client, addr = self.server_socket.accept()
                threading.Thread(target=self.serve_client, args=(client, addr), daemon=True).start()
            except socket.timeout:
                continue
            except Exception:
                break

    def serve_client(self, client, addr):
        try:
            self.after(0, self.log_srv, f"Connected: {addr[0]}:{addr[1]}")
            data = client.recv(1024)
            if data:
                req = data.decode("utf-8").strip()
                if req == "GET_TIME":
                    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
                    client.sendall(now_str.encode("utf-8"))
                    self.after(0, self.log_srv, f"Sent: {now_str}")
        except Exception as e:
            self.after(0, self.log_srv, f"Client error: {e}")
        finally:
            client.close()

    def stop_server(self):
        self.server_running = False
        if self.server_socket:
            try:
                self.server_socket.close()
            except Exception:
                pass
            self.server_socket = None

        self.srv_btn.configure(text="Start Server", fg_color="#16a34a", hover_color="#15803d")
        self.srv_host.configure(state="normal")
        self.srv_port.configure(state="normal")
        self.log_srv("Server stopped.")

    def request_time(self):
        threading.Thread(target=self.sync_worker, daemon=True).start()

    def sync_worker(self):
        host = self.cli_host.get().strip()
        try:
            port = int(self.cli_port.get().strip())
        except ValueError:
            self.after(0, self.log_cli, "Invalid port number.")
            return

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(3.0)

        start_time = time.perf_counter()
        try:
            self.after(0, self.log_cli, f"Connecting to {host}:{port}...")
            sock.connect((host, port))
            sock.sendall(b"GET_TIME\n")

            data = sock.recv(1024).decode("utf-8")
            elapsed_ms = (time.perf_counter() - start_time) * 1000

            self.after(0, self.update_client_view, data, elapsed_ms)
            self.after(0, self.log_cli, f"Received: {data}")
        except socket.timeout:
            self.after(0, self.log_cli, "Connection timed out.")
        except ConnectionRefusedError:
            self.after(0, self.log_cli, "Connection refused (server not active).")
        except Exception as e:
            self.after(0, self.log_cli, f"Error: {e}")
        finally:
            sock.close()

    def update_client_view(self, timestr, rtt):
        self.time_label.configure(text=timestr)
        self.rtt_label.configure(text=f"Delay: {rtt:.2f} ms")

if __name__ == "__main__":
    app = SimpleTimeApp()
    app.mainloop()