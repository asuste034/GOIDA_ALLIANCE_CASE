//
// Created by localuser on 6/6/26.
//

#ifndef FRONTEND_BLOCK_H
#define FRONTEND_BLOCK_H
#include <qdatetime.h>
#include <QJsonDocument>
#include <QJsonObject>
#include <QString>
#include <QJsonArray>

#include "ApiObject.h"
#include "Block.h"
;

class Block : public ApiObject {
public:
    enum BlockType {
        news, info, parking, storages
    };
private:

    BlockType type = BlockType::news;
    QString title;
    QString text;
    QDate date;
    QJsonArray images_url;

public:
    void set_type(const BlockType &type_);;

    BlockType get_type() const;;

    void set_title(const QString &title_);;

    QString get_title();;

    void set_text(const QString &text_);;

    QString get_text();;

    void set_date(const QDate &date_);;

    QDate get_date();;

    void set_images_url(const QJsonArray &image_);;

    QJsonArray get_images_url();

    QByteArray marshall();

    void unmarshall(const QByteArray& data);
};


#endif //FRONTEND_BLOCK_H
