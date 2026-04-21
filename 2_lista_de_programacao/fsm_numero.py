class FSMNumero:
    def __init__(self, numero, idioma="pt"):
        self.numero = numero
        self.idioma = idioma
        self.estado = "INICIO"
        self.resultado = ""

    def processar(self):
        while self.estado != "FIM":

            if self.estado == "INICIO":
                self._estado_inicio()

            elif self.estado == "MILHAR":
                self._estado_milhar()

            elif self.estado == "CENTENA":
                self._estado_centena()

        return self.resultado.strip()

    # =========================
    # ESTADOS
    # =========================

    def _estado_inicio(self):
        if self.numero == 0:
            self.resultado = self._zero()
            self.estado = "FIM"
        else:
            self.milhar = self.numero // 1000
            self.resto = self.numero % 1000
            self.estado = "MILHAR"

    def _estado_milhar(self):
        if self.milhar > 0:
            if self.milhar == 1:
                self.resultado += self._mil_singular()
            else:
                self.resultado += self._ate_999(self.milhar) + self._mil_plural()

        self.estado = "CENTENA"

    def _estado_centena(self):
        if self.resto > 0:
            if self.milhar > 0:
                self.resultado += self._separador()
            self.resultado += self._ate_999(self.resto)

        self.estado = "FIM"

    # =========================
    # IDIOMA
    # =========================

    def _zero(self):
        return "zero"

    def _mil_singular(self):
        return "mil " if self.idioma == "pt" else "one thousand "

    def _mil_plural(self):
        return " mil " if self.idioma == "pt" else " thousand "

    def _separador(self):
        return ", " if self.idioma == "pt" else " "

    def _ate_999(self, n):
        if self.idioma == "pt":
            return self._pt_ate_999(n)
        else:
            return self._en_ate_999(n)

    # =========================
    # PORTUGUÊS
    # =========================

    def _pt_ate_999(self, n):
        unidades = ["", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove"]
        especiais = ["dez", "onze", "doze", "treze", "quatorze", "quinze",
                     "dezesseis", "dezessete", "dezoito", "dezenove"]
        dezenas = ["", "", "vinte", "trinta", "quarenta", "cinquenta",
                   "sessenta", "setenta", "oitenta", "noventa"]
        centenas = ["", "cento", "duzentos", "trezentos", "quatrocentos",
                    "quinhentos", "seiscentos", "setecentos",
                    "oitocentos", "novecentos"]

        if n == 100:
            return "cem"

        c = n // 100
        d = (n % 100) // 10
        u = n % 10

        partes = []

        if c > 0:
            partes.append(centenas[c])

        if 10 <= n % 100 <= 19:
            partes.append(especiais[n % 100 - 10])
        else:
            if d > 0:
                partes.append(dezenas[d])
            if u > 0:
                partes.append(unidades[u])

        return " e ".join(partes)

    # =========================
    # INGLÊS
    # =========================

    def _en_ate_999(self, n):
        unidades = ["", "one", "two", "three", "four", "five", "six",
                    "seven", "eight", "nine"]
        especiais = ["ten", "eleven", "twelve", "thirteen", "fourteen",
                     "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
        dezenas = ["", "", "twenty", "thirty", "forty", "fifty",
                   "sixty", "seventy", "eighty", "ninety"]

        c = n // 100
        d = (n % 100) // 10
        u = n % 10

        partes = []

        if c > 0:
            partes.append(unidades[c] + " hundred")

        if 10 <= n % 100 <= 19:
            partes.append(especiais[n % 100 - 10])
        else:
            if d > 0:
                partes.append(dezenas[d])
            if u > 0:
                partes.append(unidades[u])

        return " ".join(partes)