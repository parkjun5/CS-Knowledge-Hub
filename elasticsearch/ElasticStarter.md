# ElasticSearch 우분투 설치

## 기본 설치 방법

1. wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -
2. sudo sh -c 'echo "deb https://artifacts.elastic.co/packages/7.x/apt stable main" > /etc/apt/sources.list.d/elastic-7.x.list'
3. sudo apt update
4. sudo apt install elasticsearch
5. sudo systemctl enable elasticsearch.service
6. sudo systemctl start elasticsearch.service

### 로그 위치

cat /var/log/elasticsearch/elasticsearch.log

### Elastic Search 설정 파일
/etc/elasticsearch/elasticsearch.yml


1. host -> network.host: 0.0.0.0
2. port -> http.port: 9200
3. 보안 설정 끄면 테스트 편함


    # Enable security features
    xpack.security.enabled: false
    
    xpack.security.enrollment.enabled: false
    
    # Enable encryption for HTTP API client connections, such as Kibana, Logstash, and Agents
    xpack.security.http.ssl:
        enabled: false
        #  keystore.path: certs/http.p12
    
    # Enable encryption and mutual authentication between cluster nodes
    xpack.security.transport.ssl:
        enabled: false
        # verification_mode: certificate
        # keystore.path: certs/transport.p12
        # truststore.path: certs/transport.p12

## 엘라스틱 서버 동작 확인

    curl -X GET "localhost:9200/"

## SELECT

    curl -XGET localhost:9200/classes?pretty
.

    curl -XGET localhost:9200/classes/_search?pretty 
    -H 'Content-Type: application/json'
    -d 
    '{
        "query": {
            "exists": {
                "field": "title"
            }
        },
        "_source": ["title"]  # 이 부분은 응답에서 'title' 필드만을 가져오기 위함입니다.
    }'
.

    curl -XGET localhost:9200/classes_2/_search?pretty
    -H 'Content-Type: application/json'
    -d
    '{
        "query": {
            "match_all": {}
        },
        "size": 100
    }'

.

    GET /classes_4/_search
    {
        "query": {
            "match": {
                "rating": 2
            }
        },
        "size": 20
    }
.

    GET /classes_4/_search
    {
        "query": {
            "bool": {
                "must": [
                    {
                        "match": {
                            "title": "Network Computer Machine"
                        }
                    }
                ],
                "must_not": [
                    {
                        "match": {
                            "Professor": "Jeniffer"
                        }
                    }
                ]
            }
        }
    }
.

    GET /classes_4/_search
    {
        "query": {
            "bool": {
                "must": [
                    {
                        "match": {
                            "title": "Network Computer Machine"
                        }
                    }
                ],
                "filter": [
                    {
                        "bool": {
                            "must_not": [
                                {
                                    "match": {
                                        "Professor": "Jeniffer"
                                    }
                                }
                            ]
                        }
                    }
                ],
                "should": [
                    {
                        "match": {
                            "semester": "spring"
                        }
                    },
                    {
                        "match": {
                            "semester": "fall"
                        }
                    },
                    {
                        "bool": {
                            "must": [
                                {
                                    "match": {
                                        "semester": "spring"
                                    }
                                },
                                {
                                    "match": {
                                        "semester": "fall"
                                    }
                                }
                            ],
                        "boost": 2
                        }
                    }
                ]
            }
        }
    }
.

    GET /classes_4/_search
    {
        "query": {
            "range": {
                "student_count": {
                    "gte": 30,
                    "lt": 50
                }
            }
        }
    }

## INSERT

    curl -XPUT localhost:9200/classes/_doc
    -H 'Content-Type: application/json'
    -d
    '{
        "title" : "DDD",
        "professor" : "TOM"
    }'
.
    
    curl -XPOST localhost:9200/classes/_doc/
    -d @classExample.json
    -H 'Content-Type: application/json'
.


## UPDATE

    curl -XPUT localhost:9200/classes/_doc/1 -H 'Content-Type: application/json' -d '{
        "doc": {
            "title" : "ATDD",
            "professor" : "JASON"
        }
    }'

#### add one more field

    curl -XPOST "localhost:9200/classes/_update/1"
    -H 'Content-Type: application/json'
    -d
    '{
        "doc": {
            "location": "Room A"
        }
    }'
.

    curl -XPUT localhost:9200/classes/_doc/1
    -H 'Content-Type: application/json'
    -d
    '{
        "title": "ATDD",
        "professor": "jsaoon"
    }'
.

    curl -XPOST "localhost:9200/classes/_update/1"
    -H 'Content-Type: application/json'
    -d
    '{
        "script": "ctx._source.count += 18"
    }'

## Class Mapping

클래스에 속성을 매핑

    curl -XPUT "localhost:9200/classes_4/_mapping"
    -H 'Content-Type: application/json'
    --data-binary @classesRatingMapping.json


