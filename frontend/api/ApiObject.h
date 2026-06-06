//
// Created by localuser on 6/6/26.
//

#ifndef FRONTEND_APIOBJECT_H
#define FRONTEND_APIOBJECT_H
#include <QByteArray>

class ApiObject {
public:
    virtual ~ApiObject() = default;
    virtual QByteArray marshall() = 0;
    virtual void unmarshall(const QByteArray &data) = 0;
};


#endif //FRONTEND_APIOBJECT_H
