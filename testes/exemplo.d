// exemplo de programa em D usado para testar o analisador lexico
// cobre todos os tokens da linguagem

int soma(int a, int &b, float c[]) {
    int i, total[];
    float media;
    string nome;

    total = [1, 2, 3];
    i = 0;
    media = 0.5;
    nome = "resultado: \"parcial\"";

    while (i < 3) {
        total[i] = total[i] + a * 2 - b / 2;   // nao e comentario aqui: a / e divisao
        i = i + 1;
        if (i >= 2 AND i != 3) {
            media = media + 1.75;
        } elif (i <= 0 OR NOT i == 0) {
            continue;
        } else {
            break;
        }
    }

    for (i in total) {
        write(i, " ", nome);
    }

    for (i = 0; i > 5; ++i) {
        --i;
        media = media * 7 div 2 mod 3;
    }

    loop {
        read(nome);
        a = str2int(nome);
        media = str2float(nome);
        nome = int2str(a);
        nome = float2string(media);
        break;
    }

    // case sensitive: While, Total e OR_ sao identificadores comuns
    While = 1;
    Total_1 = 2;
    return a;
}

void main() {
    write("fim");
}
