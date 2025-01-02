# Copyleft 🄯, Germano Castanho, 2024
# Software livre licenciado sob a GPL-3.0
# Cada linha, um manifesto pela liberdade

from interface.config_interface import exibir_configuracoes
from interface.estado_sessao import preparar_estado_sessao
from interface.ui_principal import configurar_pagina, exibir_conversa


def main():
    configurar_pagina()
    preparar_estado_sessao()
    exibir_configuracoes()
    exibir_conversa()


if __name__ == "__main__":
    main()
