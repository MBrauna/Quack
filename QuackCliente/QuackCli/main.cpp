#include "quackvisual.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    QuackVisual w;
    w.show();

    return a.exec();
}
