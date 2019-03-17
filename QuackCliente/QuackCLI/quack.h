#ifndef QUACK_H
#define QUACK_H

#include <QWidget>

namespace Ui {
class Quack;
}

class Quack : public QWidget
{
    Q_OBJECT

public:
    explicit Quack(QWidget *parent = 0);
    ~Quack();

private:
    Ui::Quack *ui;
};

#endif // QUACK_H
