#include "quack.h"
#include "ui_quack.h"

Quack::Quack(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::Quack)
{
    ui->setupUi(this);

    // Permite que o fundo fique transparente.
    setAttribute(Qt::WA_TranslucentBackground);
    setWindowFlags(Qt::FramelessWindowHint);

    // ALtera a logo do projeto
}

Quack::~Quack()
{
    delete ui;
}

void Quack::on_quack_btn_fechar_pressed()
{
    Quack::close();
}

void Quack::on_quack_btn_minimizar_pressed()
{
    Quack::showMinimized();
}
