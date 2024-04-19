    GET /_cat/indices?v
_

    GET opensearch_dashboards_sample_data_ecommerce/_search
    {
        "size": 10
    }
_

    GET opensearch_dashboards_sample_data_ecommerce/_search
    {
        "size": 0,
        "query": {
            "match": {
                "currency": "EUR"
            }
        },
        "aggs": {
            "avg_price": {
            "avg": {
                "field": "products.price"
            }
        },
        "max_taxful_price": {
            "max": {
                "field": "products.price"
            }
        },
        "min_price": {
            "min": {
                "field": "products.price"
            }
        },
        "sum_price": {
            "sum": {
                "field": "products.price"
            }
        },
        "count_price": {
            "value_count": {
                "field": "products.price"
            }
        },
        "stats_price": {
            "stats": {
                "field": "products.price"
            }
        },
        "filter_count_price": {
            "filter": {
                "bool": {
                    "must": [
                        {
                            "match": {
                                "geoip.city_name": "Cairo"
                            }
                        }
                    ]
                }
            }
        },
        "filter_sum_price": {
            "filter": {
                "bool": {
                    "must": [
                        {
                            "match": {
                                "geoip.city_name": "Cairo"
                            }
                        }
                    ]
                }
            },
                "aggs": {
                    "stat_filter_price": {
                        "stats": {
                            "field": "products.price"
                        }
                    }
                }
            }
        }
    }
_

    GET opensearch_dashboards_sample_data_ecommerce/_search
    {
        "query": {
            "match": {
                "customer_gender": "MALE"
            }
        },
        "_source": ["products"]  
    }
_

    GET opensearch_dashboards_sample_data_ecommerce/_search
    {
        "query": {
            "terms": {
                "customer_gender": [ "", "FEMALE" ]
            }
        },
        "_source": ["products"]  
    }
_

    GET opensearch_dashboards_sample_data_ecommerce/_search
    {
        "size": 3,
        "query": {
            "bool": {
                "should": [
                    {
                        "wildcard": {
                            "email": {
                                "value": "*@riley-family.zzz",
                                "boost": 2.0
                            }
                        }
                    },
                    {
                        "term": {
                            "customer_gender": {
                                "value": "MALE",
                                "boost": 1.0
                            }
                        }
                    },
                    {
                        "range": {
                            "order_date": {
                                "gte": "2024-02-01",
                                "lte": "2024-02-04",
                                "time_zone": "+09:00",
                                "boost": 2.0
                            }
                        }
                    },
                    {
                        "term": {
                            "currency": {
                                "value" : [
                                    "EUR",
                                    "KOR"
                                ],
                                "boost": 0.5
                            }
                        }
                    }
                ]
            }
        },
        "_source": [
            "currency",
            "customer_full_name",
            "email",
            "order_date",
            "order_id"
        ]  
    }
