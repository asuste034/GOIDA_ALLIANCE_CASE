//
// Created by localuser on 6/6/26.
//

#include "Block.h"

void Block::set_type(const BlockType &type_) {
    type = type_;
}

Block::BlockType Block::get_type() const {
    return type;
}

void Block::set_title(const QString &title_) {
    title = title_;
}

QString Block::get_title() {
    return title;
}

void Block::set_text(const QString &text_) {
    text = text_;
}

QString Block::get_text() {
    return text;
}

void Block::set_date(const QDate &date_) {
    date = date_;
}

QDate Block::get_date() {
    return date;
}

void Block::set_images_url(const QJsonArray &image_) {
    images_url = image_;
}

QJsonArray Block::get_images_url() {
    return images_url;
}

QByteArray Block::marshall() {
    QJsonObject obj;
    switch (type) {
        case news:
            obj["type"] = "news";
            break;
        case info:
            obj["type"] = "info";
            break;
        case parking:
            obj["type"] = "parking";
            break;
        case storages:
            obj["type"] = "storages";
            break;
    }

    obj["title"] = title;
    obj["text"] = text;
    obj["date"] = date.toString();
    obj["images_url"] = images_url;

    return QJsonDocument(obj).toJson();
}

void Block::unmarshall(const QByteArray &data) {
    QJsonDocument doc = QJsonDocument::fromVariant(QCborValue::fromCbor(data).toVariant());

    if (doc["type"].toString() == "news")
        type = news;
    if (doc["type"].toString() == "info")
        type = info;
    if (doc["type"].toString() == "parking")
        type = parking;
    if (doc["type"].toString() == "storages")
        type = storages;

    title = doc["title"].toString();
    text = doc["text"].toString();
    date = QDate::fromString(doc["date"].toString());
    images_url = doc["images_url"].toArray();
}
