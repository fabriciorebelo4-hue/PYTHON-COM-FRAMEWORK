import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import datetime

class CaixaEletronicoApp:
    def __init__(self, root):
        # --- Configurações da Janela Principal ---
        self.root = root
        self.root.title("Banco Python")
        self.root.geometry("400x500") # Largura x Altura
        self.root.resizable(False, False) # Impede redimensionar a janela
        self.root.configure(bg="#f4f4f9") # Cor de fundo cinza bem claro

        # --- Variáveis de Estado do Banco ---
        self.senha_correta = "123456"
        self.tentativas = 3
        self.saldo = 0.0
        self.limite_emprestimo = 5000.0
        self.extrato = []

        # Estilo visual moderno usando ttk
        self.style = ttk.Style()
        self.style.theme_use('clam') # Tema com visual mais "flat" e limpo
        self.style.configure("TButton", font=("Helvetica", 11, "bold"), padding=10)
        self.style.configure("TLabel", background="#f4f4f9", font=("Helvetica", 12))

        # Inicializa a tela de login
        self.tela_login()

    # ==========================================
    # TELA DE LOGIN
    # ==========================================
    def tela_login(self):
        # Frame é como um "container" ou caixa para agrupar elementos
        self.frame_login = tk.Frame(self.root, bg="#f4f4f9")
        self.frame_login.pack(expand=True, fill="both", pady=50)

        # Título
        lbl_titulo = tk.Label(self.frame_login, text="🏦 BANCO PYTHON", font=("Helvetica", 20, "bold"), bg="#f4f4f9", fg="#2c3e50")
        lbl_titulo.pack(pady=20)

        lbl_instrucao = ttk.Label(self.frame_login, text="Digite sua senha de 6 dígitos:")
        lbl_instrucao.pack(pady=5)

        # Caixa de entrada para a senha (o parâmetro 'show' oculta os caracteres)
        self.entry_senha = ttk.Entry(self.frame_login, show="*", font=("Helvetica", 14), justify="center")
        self.entry_senha.pack(pady=10)

        # Botão que aciona a função de verificar a senha
        btn_entrar = ttk.Button(self.frame_login, text="ACESSAR CONTA", command=self.verificar_senha)
        btn_entrar.pack(pady=20)

    def verificar_senha(self):
        senha_digitada = self.entry_senha.get()

        if senha_digitada == self.senha_correta:
            # Destroi a tela de login e carrega a tela do menu principal
            self.frame_login.destroy()
            self.tela_principal()
        else:
            self.tentativas -= 1
            if self.tentativas > 0:
                # Exibe um popup de erro
                messagebox.showerror("Erro", f"Senha incorreta!\nVocê tem {self.tentativas} tentativa(s).")
                self.entry_senha.delete(0, tk.END) # Limpa o campo digitado
            else:
                messagebox.showerror("Bloqueado", "Conta bloqueada por segurança. O aplicativo será encerrado.")
                self.root.destroy() # Encerra o programa

    # ==========================================
    # TELA PRINCIPAL (MENU)
    # ==========================================
    def tela_principal(self):
        self.frame_principal = tk.Frame(self.root, bg="#f4f4f9")
        self.frame_principal.pack(expand=True, fill="both")

        # Cabeçalho
        header = tk.Frame(self.frame_principal, bg="#2c3e50", height=80)
        header.pack(fill="x")
        
        lbl_boas_vindas = tk.Label(header, text="Olá, Cliente!", font=("Helvetica", 16, "bold"), bg="#2c3e50", fg="white")
        lbl_boas_vindas.pack(pady=10)

        # Label dinâmica para mostrar o saldo atualizado
        self.lbl_saldo = tk.Label(header, text=f"Saldo atual: R$ {self.saldo:.2f}", font=("Helvetica", 14), bg="#2c3e50", fg="#2ecc71")
        self.lbl_saldo.pack(pady=5)

        # Container dos botões
        frame_botoes = tk.Frame(self.frame_principal, bg="#f4f4f9")
        frame_botoes.pack(pady=30)

        # Criação dos botões vinculados às suas respectivas funções
        ttk.Button(frame_botoes, text="💵 Depositar", command=self.depositar).pack(fill="x", pady=5, ipadx=50)
        ttk.Button(frame_botoes, text="🏧 Sacar", command=self.sacar).pack(fill="x", pady=5)
        ttk.Button(frame_botoes, text="🤝 Empréstimo", command=self.emprestimo).pack(fill="x", pady=5)
        ttk.Button(frame_botoes, text="📄 Ver Extrato", command=self.ver_extrato).pack(fill="x", pady=5)
        ttk.Button(frame_botoes, text="🚪 Sair", command=self.root.destroy).pack(fill="x", pady=20)

    # Função para atualizar o texto do saldo na tela principal
    def atualizar_saldo_tela(self):
        self.lbl_saldo.config(text=f"Saldo atual: R$ {self.saldo:.2f}")

    # ==========================================
    # FUNÇÕES DE OPERAÇÃO BANCÁRIA
    # ==========================================
    def depositar(self):
        # Abre uma janela de diálogo para digitar um número flutuante
        valor = simpledialog.askfloat("Depósito", "Digite o valor para depósito (R$):", minvalue=0.01)
        if valor:
            self.saldo += valor
            data_hora = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
            self.extrato.append(f"[{data_hora}] + Depósito: R$ {valor:.2f}")
            self.atualizar_saldo_tela()
            messagebox.showinfo("Sucesso", f"Depósito de R$ {valor:.2f} realizado!")

    def sacar(self):
        valor = simpledialog.askfloat("Saque", "Digite o valor para saque (R$):", minvalue=0.01)
        if valor:
            if valor > self.saldo:
                messagebox.showwarning("Aviso", "Saldo insuficiente para esta operação.")
            else:
                self.saldo -= valor
                data_hora = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
                self.extrato.append(f"[{data_hora}] - Saque: R$ {valor:.2f}")
                self.atualizar_saldo_tela()
                messagebox.showinfo("Sucesso", f"Saque de R$ {valor:.2f} realizado!\nRetire o dinheiro.")

    def emprestimo(self):
        msg = f"Limite pré-aprovado: R$ {self.limite_emprestimo:.2f}\n\nQuanto deseja pegar emprestado?"
        valor = simpledialog.askfloat("Empréstimo", msg, minvalue=0.01)
        if valor:
            if valor > self.limite_emprestimo:
                messagebox.showwarning("Aviso", "Valor solicitado excede seu limite pré-aprovado.")
            else:
                self.saldo += valor
                self.limite_emprestimo -= valor
                data_hora = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
                self.extrato.append(f"[{data_hora}] + Empréstimo: R$ {valor:.2f}")
                self.atualizar_saldo_tela()
                messagebox.showinfo("Sucesso", f"Empréstimo de R$ {valor:.2f} creditado na sua conta!")

    def ver_extrato(self):
        # Cria uma nova janela (Toplevel) para mostrar o extrato por cima da principal
        janela_extrato = tk.Toplevel(self.root)
        janela_extrato.title("Extrato Bancário")
        janela_extrato.geometry("350x400")
        janela_extrato.configure(bg="white")

        tk.Label(janela_extrato, text="Histórico de Movimentações", font=("Helvetica", 14, "bold"), bg="white").pack(pady=10)

        # Widget Text serve para mostrar múltiplas linhas de texto
        caixa_texto = tk.Text(janela_extrato, width=40, height=15, font=("Courier", 10), bg="#f9f9f9", state="normal")
        caixa_texto.pack(pady=10, padx=10)

        if not self.extrato:
            caixa_texto.insert(tk.END, "Nenhuma movimentação realizada.")
        else:
            for operacao in self.extrato:
                caixa_texto.insert(tk.END, operacao + "\n")
        
        caixa_texto.insert(tk.END, "-"*35 + "\n")
        caixa_texto.insert(tk.END, f"SALDO ATUAL: R$ {self.saldo:.2f}")

        # Desabilita a edição da caixa de texto para o usuário não apagar o extrato
        caixa_texto.configure(state="disabled")

# ==========================================
# INICIALIZAÇÃO DO PROGRAMA
# ==========================================
if __name__ == "__main__":
    # Cria a janela "raiz" (root) do sistema operacional
    root = tk.Tk()
    # Instancia a nossa classe passando a janela raiz para ela
    app = CaixaEletronicoApp(root)
    # Roda o loop principal (mantém a janela aberta esperando cliques)
    root.mainloop()