#include "quack.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    Quack quackprincipal;
    quackprincipal.show();

    return a.exec();
}
