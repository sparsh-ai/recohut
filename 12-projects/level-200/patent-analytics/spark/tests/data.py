import pyspark.sql.types as t
from datetime import datetime


class CleanedData:
    patent = [
        (
            "6114900",
            "utility",
            datetime(2000, 9, 5),
            "A semiconductor memory device",
            "Semiconductor memory device ",
            "A",
            2,
        ),
        (
            "D419739",
            "utility",
            datetime(2011, 1, 3),
            "This process for the production of 2-keto-D",
            "Manufacturing independent constant current power",
            "S",
            3,
        ),
        (
            "6018034",
            "utility",
            datetime(2011, 1, 3),
            "A method of manufacturing a small",
            "Process for the production of 2-keto-D",
            "A",
            4,
        ),
    ]
    patent_schema = t.StructType(
        [
            t.StructField("id", t.StringType(), False),
            t.StructField("type", t.StringType(), False),
            t.StructField("date", t.DateType(), False),
            t.StructField("title", t.StringType(), False),
            t.StructField("abstract", t.StringType(), True),
            t.StructField("kind", t.StringType(), False),
            t.StructField("num_claims", t.IntegerType(), False),
        ]
    )

    wipo = [("6114900", 1), ("D419739", 2), ("6018034", 3)]

    wipo_schema = t.StructType(
        [
            t.StructField("patent_id", t.StringType(), False),
            t.StructField("field_id", t.IntegerType(), False),
        ]
    )

    wipo_field = [
        (1, "Electrical engineering", "Electrical machinery, apparatus"),
        (2, "Instruments", "Measurement"),
        (3, "Instruments", "Control"),
    ]

    wipo_field_schema = t.StructType(
        [
            t.StructField("id", t.IntegerType(), False),
            t.StructField("sector_title", t.StringType(), False),
            t.StructField("field_title", t.StringType(), False),
        ]
    )

    location = [
        (
            "7674c183-cb8f-11eb-9615-121df0c29c1e",
            "1af00b874ff3183021ca5c541e6f3e8d1bbb2b412bdb87f44cb07ae930dad646",
            "Albania",
            "EU",
        ),
        (
            "6647cd94-cbae-11eb-9615-121df0c29c1e",
            "49dca65f362fee401292ed7ada96f96295eab1e589c52e4e66bf4aedda715fdd",
            "United States",
            "NA",
        ),
    ]

    location_schema = t.StructType(
        [
            t.StructField("id", t.StringType(), False),
            t.StructField("new_id", t.StringType(), False),
            t.StructField("Country", t.StringType(), False),
            t.StructField("Continent", t.StringType(), False),
        ]
    )

    patent_assignee = [("6114900", "cf06cbad-b4f3-45f7-888a-c0d078f5b856", None)]

    patent_assignee_schema = t.StructType(
        [
            t.StructField("patent_id", t.StringType(), False),
            t.StructField("assignee_id", t.StringType(), False),
            t.StructField("location_id", t.StringType(), True),
        ]
    )

    assignee = [
        (
            "cf06cbad-b4f3-45f7-888a-c0d078f5b856",
            "Rainbow Display, Inc.",
            "company",
            "23d67e983020b217078bba89b0b8de9f00e41f742669dad1090bde4044bf9dd6",
        )
    ]

    assignee_schema = t.StructType(
        [
            t.StructField("id", t.StringType(), False),
            t.StructField("name", t.StringType(), False),
            t.StructField("type", t.StringType(), False),
            t.StructField("new_id", t.StringType(), False),
        ]
    )

    patent_inventor = [
        ("D419739", "fl:a._ln:george-1", "7674c183-cb8f-11eb-9615-121df0c29c1e")
    ]

    patent_inventor_schema = t.StructType(
        [
            t.StructField("patent_id", t.StringType(), False),
            t.StructField("inventor_id", t.StringType(), False),
            t.StructField("location_id", t.StringType(), True),
        ]
    )

    inventor = [
        (
            "fl:a._ln:george-1",
            "individual",
            "A. Chacko George",
            "73b561e3245e37e271ada78c73f5b2112b2394393ed3ae39e1e7ee311db87657",
        )
    ]

    inventor_schema = t.StructType(
        [
            t.StructField("id", t.StringType(), False),
            t.StructField("type", t.StringType(), False),
            t.StructField("name", t.StringType(), False),
            t.StructField("new_id", t.StringType(), False),
        ]
    )

    intermediary_patent = [
        (
            "6114900",
            "23d67e983020b217078bba89b0b8de9f00e41f742669dad1090bde4044bf9dd6",
            "Rainbow Display, Inc.",
            "company",
            None,
            None,
            None,
        ),
        (
            "D419739",
            "73b561e3245e37e271ada78c73f5b2112b2394393ed3ae39e1e7ee311db87657",
            "A. Chacko George",
            "individual",
            "1af00b874ff3183021ca5c541e6f3e8d1bbb2b412bdb87f44cb07ae930dad646",
            "Albania",
            "EU",
        ),
        ("6018034", None, None, None, None, None, None),
    ]

    intermediary_patent_schema = t.StructType(
        [
            t.StructField("id", t.StringType(), False),
            t.StructField("owner_id", t.StringType(), True),
            t.StructField("name", t.StringType(), True),
            t.StructField("type", t.StringType(), True),
            t.StructField("location_id", t.StringType(), True),
            t.StructField("country", t.StringType(), True),
            t.StructField("continent", t.StringType(), True),
        ]
    )


class KeywordExtractionData:
    patent_keyword_raw = [
        (
            "6114900",
            [
                ("chunk", 20, 27, "test2", {"score": "0.2"}, []),
                ("chunk", 1, 10, "test3", {"score": "0.3"}, []),
                ("chunk", 12, 18, "test", {"score": "0.1"}, []),
            ],
        ),
        (
            "D419739",
            [
                ("chunk", 12, 18, "semiconductor", {"score": "0.1"}, []),
                ("chunk", 28, 32, "pool", {"score": "0.2"}, []),
            ],
        ),
        ("6018034", [("chunk", 12, 18, "mechanic", {"score": "0.1"}, [])]),
    ]

    patent_keyword_raw_schema = t.StructType(
        [
            t.StructField("id", t.StringType(), False),
            t.StructField(
                "keywords",
                t.ArrayType(
                    t.StructType(
                        [
                            t.StructField("annotatorType", t.StringType(), True),
                            t.StructField("begin", t.IntegerType(), True),
                            t.StructField("end", t.IntegerType(), True),
                            t.StructField("result", t.StringType(), True),
                            t.StructField(
                                "metadata",
                                t.MapType(t.StringType(), t.StringType(), True),
                            ),
                            t.StructField(
                                "embeddings", t.ArrayType(t.FloatType()), True
                            ),
                        ]
                    ),
                    False,
                ),
            ),
        ]
    )

    patent_keyword = [
        ("6114900", "test", "0.1", 1),
        ("6114900", "test2", "0.2", 2),
        ("6114900", "test3", "0.3", 3),
        ("D419739", "semiconductor", "0.1", 1),
        ("D419739", "pool", "0.2", 2),
        ("6018034", "mechanic", "0.1", 1),
    ]

    patent_keyword_schema = t.StructType(
        [
            t.StructField("id", t.StringType(), False),
            t.StructField("keyword", t.StringType(), True),
            t.StructField("score", t.StringType(), True),
            t.StructField("row", t.IntegerType(), True),
        ]
    )


class RawData:
    patent = [
        (
            "6114900",
            "utility",
            "6114900",
            "US",
            datetime(2000, 9, 5),
            "A semiconductor memory device",
            "Semiconductor memory device ",
            "A",
            2,
            "ipg161011.xml",
            0,
        ),
        (
            "D419739",
            "utility",
            "D419739",
            "US",
            datetime(2011, 1, 3),
            "This process for the production of 2-keto-D",
            "Manufacturing independent constant current power",
            "S",
            3,
            "ipg070320.xml",
            0,
        ),
        (
            "6018034",
            "utility",
            "6018034",
            "US",
            datetime(2011, 1, 3),
            "A method of manufacturing a small",
            "Process for the production of 2-keto-D",
            "A",
            4,
            "ipg140114.xml",
            0,
        ),
        (
            "D547004",
            "utility",
            "D547004",
            "US",
            datetime(1999, 1, 3),
            "Hair treatment",
            None,
            "S1",
            1,
            "ipg070717.xml",
            0,
        ),
    ]

    patent_schema = t.StructType(
        [
            t.StructField("id", t.StringType(), False),
            t.StructField("type", t.StringType(), False),
            t.StructField("number", t.StringType(), False),
            t.StructField("country", t.StringType(), False),
            t.StructField("date", t.DateType(), False),
            t.StructField("title", t.StringType(), False),
            t.StructField("abstract", t.StringType(), True),
            t.StructField("kind", t.StringType(), False),
            t.StructField("num_claims", t.IntegerType(), False),
            t.StructField("filename", t.StringType(), False),
            t.StructField("withdrawn", t.IntegerType(), False),
        ]
    )

    assignee = [
        (
            "cf06cbad-b4f3-45f7-888a-c0d078f5b856",
            2.0,
            None,
            None,
            "Rainbow Display, Inc.",
        ),
        ("d7f6cbad-b4f3-45f7-888a-c0d078f5b856", 1.0, "Abel", "Thomas", None),
    ]

    assignee_schema = t.StructType(
        [
            t.StructField("id", t.StringType(), False),
            t.StructField("type", t.DoubleType(), False),
            t.StructField("name_first", t.StringType(), True),
            t.StructField("name_last", t.StringType(), True),
            t.StructField("organization", t.StringType(), True),
        ]
    )

    country_shapes = [
        (
            "FeatureCollection",
            [
                (
                    "Feature",
                    ("49518",),
                    (
                        "Polygon",
                        [
                            [
                                [29.96, -2.327],
                                [29.919, -2.703],
                                [29.724, -2.819],
                                [29.438, -2.798],
                                [29.371, -2.84],
                                [29.326, -2.654],
                                [29.15, -2.592],
                                [29.062, -2.602],
                                [29.04, -2.745],
                                [28.897, -2.66],
                                [28.862, -2.531],
                                [28.884, -2.393],
                                [29.119, -2.249],
                                [29.175, -2.119],
                                [29.136, -1.86],
                                [29.362, -1.509],
                                [29.45, -1.506],
                                [29.566, -1.387],
                                [29.66, -1.393],
                                [29.735, -1.34],
                                [29.796, -1.373],
                                [29.824, -1.309],
                                [29.883, -1.356],
                                [29.915, -1.482],
                                [30.052, -1.431],
                                [30.345, -1.131],
                                [30.352, -1.062],
                                [30.47, -1.053],
                                [30.47, -1.156],
                                [30.569, -1.337],
                                [30.738, -1.445],
                                [30.839, -1.651],
                                [30.808, -1.938],
                                [30.9, -2.078],
                                [30.844, -2.206],
                                [30.857, -2.315],
                                [30.782, -2.391],
                                [30.716, -2.357],
                                [30.569, -2.42],
                                [30.409, -2.311],
                                [30.136, -2.438],
                                [29.96, -2.327],
                            ]
                        ],
                    ),
                ),
                (
                    "Feature",
                    ("783754",),
                    (
                        "MultiPolygon",
                        [
                            [
                                [
                                    [19.274, 40.491],
                                    [19.268, 40.494],
                                    [19.271, 40.514],
                                    [19.286, 40.474],
                                    [19.274, 40.491],
                                ]
                            ],
                            [
                                [
                                    [19.394, 40.897],
                                    [19.394, 40.897],
                                    [19.396, 40.89],
                                    [19.394, 40.897],
                                ]
                            ],
                            [
                                [
                                    [19.443, 41.432],
                                    [19.452, 41.419],
                                    [19.444, 41.408],
                                    [19.448, 41.423],
                                    [19.443, 41.432],
                                ]
                            ],
                            [
                                [
                                    [19.444, 41.433],
                                    [19.446, 41.433],
                                    [19.445, 41.432],
                                    [19.444, 41.433],
                                ]
                            ],
                            [
                                [
                                    [19.471, 41.444],
                                    [19.515, 41.521],
                                    [19.444, 41.588],
                                    [19.563, 41.579],
                                    [19.585, 41.643],
                                    [19.603, 41.61],
                                    [19.609, 41.627],
                                    [19.599, 41.638],
                                    [19.605, 41.644],
                                    [19.603, 41.65],
                                    [19.566, 41.654],
                                    [19.583, 41.706],
                                    [19.57, 41.749],
                                    [19.572, 41.763],
                                    [19.602, 41.79],
                                    [19.443, 41.887],
                                    [19.371, 41.844],
                                    [19.378, 42.072],
                                    [19.493, 42.053],
                                    [19.358, 42.236],
                                    [19.662, 42.628],
                                    [19.756, 42.637],
                                    [19.743, 42.545],
                                    [19.831, 42.466],
                                    [20.088, 42.552],
                                    [20.221, 42.433],
                                    [20.246, 42.324],
                                    [20.339, 42.328],
                                    [20.515, 42.224],
                                    [20.627, 41.961],
                                    [20.514, 41.728],
                                    [20.558, 41.582],
                                    [20.457, 41.551],
                                    [20.561, 41.405],
                                    [20.491, 41.333],
                                    [20.515, 41.231],
                                    [20.647, 41.069],
                                    [20.651, 40.907],
                                    [20.968, 40.911],
                                    [20.921, 40.886],
                                    [20.966, 40.849],
                                    [20.905, 40.771],
                                    [20.984, 40.801],
                                    [20.956, 40.77],
                                    [21.032, 40.699],
                                    [20.987, 40.672],
                                    [21.038, 40.69],
                                    [21.057, 40.617],
                                    [20.957, 40.47],
                                    [20.843, 40.48],
                                    [20.787, 40.429],
                                    [20.678, 40.095],
                                    [20.45, 40.074],
                                    [20.394, 39.996],
                                    [20.312, 39.991],
                                    [20.414, 39.815],
                                    [20.29, 39.805],
                                    [20.322, 39.729],
                                    [20.229, 39.65],
                                    [19.983, 39.689],
                                    [20.02, 39.859],
                                    [19.912, 39.905],
                                    [19.937, 39.942],
                                    [19.866, 40.034],
                                    [19.471, 40.215],
                                    [19.288, 40.422],
                                    [19.379, 40.407],
                                    [19.436, 40.312],
                                    [19.485, 40.348],
                                    [19.494, 40.447],
                                    [19.404, 40.499],
                                    [19.377, 40.539],
                                    [19.448, 40.495],
                                    [19.456, 40.556],
                                    [19.385, 40.543],
                                    [19.305, 40.66],
                                    [19.367, 40.715],
                                    [19.393, 40.903],
                                    [19.478, 40.97],
                                    [19.436, 41.001],
                                    [19.437, 41.146],
                                    [19.519, 41.267],
                                    [19.421, 41.325],
                                    [19.391, 41.414],
                                    [19.471, 41.444],
                                ],
                                [
                                    [19.603, 41.61],
                                    [19.603, 41.61],
                                    [19.603, 41.61],
                                    [19.603, 41.61],
                                ],
                                [
                                    [19.604, 41.61],
                                    [19.61, 41.619],
                                    [19.603, 41.61],
                                    [19.604, 41.61],
                                ],
                                [
                                    [19.412, 40.878],
                                    [19.412, 40.879],
                                    [19.411, 40.878],
                                    [19.412, 40.878],
                                ],
                                [
                                    [19.403, 40.86],
                                    [19.419, 40.864],
                                    [19.412, 40.878],
                                    [19.403, 40.86],
                                ],
                                [
                                    [19.412, 40.899],
                                    [19.412, 40.899],
                                    [19.412, 40.899],
                                    [19.412, 40.899],
                                ],
                                [
                                    [19.417, 40.899],
                                    [19.415, 40.904],
                                    [19.412, 40.899],
                                    [19.417, 40.899],
                                ],
                                [
                                    [20.051, 39.757],
                                    [20.05, 39.802],
                                    [20.018, 39.813],
                                    [20.018, 39.747],
                                    [20.051, 39.757],
                                ],
                                [
                                    [19.488, 40.893],
                                    [19.529, 40.929],
                                    [19.499, 40.984],
                                    [19.443, 40.887],
                                    [19.488, 40.893],
                                ],
                                [
                                    [19.481, 40.986],
                                    [19.478, 41.003],
                                    [19.474, 41.004],
                                    [19.473, 40.995],
                                    [19.481, 40.986],
                                ],
                                [
                                    [19.605, 41.773],
                                    [19.573, 41.759],
                                    [19.571, 41.752],
                                    [19.609, 41.762],
                                    [19.618, 41.783],
                                    [19.605, 41.773],
                                ],
                                [
                                    [19.592, 41.747],
                                    [19.581, 41.731],
                                    [19.587, 41.71],
                                    [19.583, 41.732],
                                    [19.612, 41.726],
                                    [19.592, 41.747],
                                ],
                                [
                                    [19.595, 41.713],
                                    [19.594, 41.714],
                                    [19.59, 41.715],
                                    [19.595, 41.713],
                                ],
                                [
                                    [19.598, 41.714],
                                    [19.588, 41.723],
                                    [19.594, 41.714],
                                    [19.598, 41.714],
                                ],
                                [
                                    [19.615, 41.719],
                                    [19.61, 41.725],
                                    [19.609, 41.725],
                                    [19.615, 41.719],
                                ],
                                [
                                    [19.616, 41.719],
                                    [19.617, 41.726],
                                    [19.615, 41.72],
                                    [19.616, 41.719],
                                ],
                            ],
                            [
                                [
                                    [19.445, 40.941],
                                    [19.461, 40.946],
                                    [19.467, 40.945],
                                    [19.467, 40.945],
                                    [19.445, 40.941],
                                ]
                            ],
                        ],
                    ),
                ),
            ],
        )
    ]

    country_shapes_schema = t.StructType(
        [
            t.StructField("type", t.StringType(), False),
            t.StructField(
                "features",
                t.ArrayType(
                    t.StructType(
                        [
                            t.StructField("type", t.StringType(), False),
                            t.StructField(
                                "properties",
                                t.StructType(
                                    [t.StructField("geoNameId", t.StringType(), False)]
                                ),
                            ),
                            t.StructField(
                                "geometry",
                                t.StructType(
                                    [
                                        t.StructField("type", t.StringType(), False),
                                        t.StructField(
                                            "coordinates",
                                            t.ArrayType(
                                                t.ArrayType(
                                                    t.ArrayType(t.StringType(), False)
                                                )
                                            ),
                                        ),
                                    ]
                                ),
                            ),
                        ]
                    )
                ),
            ),
        ]
    )

    location = [
        (
            "7674c183-cb8f-11eb-9615-121df0c29c1e",
            None,
            None,
            None,
            41.420871,
            20.017932,
            None,
            None,
            None,
        ),
        (
            "6647cd94-cbae-11eb-9615-121df0c29c1e",
            None,
            "MD",
            None,
            None,
            None,
            None,
            None,
            None,
        ),
    ]

    location_schma = t.StructType(
        [
            t.StructField("id", t.StringType(), False),
            t.StructField("city", t.StringType(), True),
            t.StructField("state", t.StringType(), True),
            t.StructField("country", t.StringType(), True),
            t.StructField("latitude", t.DoubleType(), True),
            t.StructField("longitude", t.DoubleType(), True),
            t.StructField("county", t.StringType(), True),
            t.StructField("state_fips", t.DoubleType(), True),
            t.StructField("county_fips", t.IntegerType(), True),
        ]
    )

    wipo = [("6114900", 1, 0), ("6114900", 1, 1), ("D419739", 2, 0), ("6018034", 3, 0)]
    wipo_schema = t.StructType(
        [
            t.StructField("patent_id", t.StringType(), False),
            t.StructField("field_id", t.IntegerType(), False),
            t.StructField("sequence", t.IntegerType(), False),
        ]
    )

    wipo_field = [
        ("1", "Electrical engineering", "Electrical machinery, apparatus"),
        ("2", "Instruments", "Measurement"),
        ("3", "Instruments", "Control"),
        ("D1", "Electrical engineering", "Electrical machinery, apparatus"),
        ("D2", "Instruments", "Measurement"),
    ]

    wipo_field_schema = t.StructType(
        [
            t.StructField("id", t.StringType(), False),
            t.StructField("sector_title", t.StringType(), False),
            t.StructField("field_title", t.StringType(), False),
        ]
    )

    inventor = [("fl:a._ln:george-1", "A. Chacko", "George", 1.0, 1)]

    inventor_schema = t.StructType(
        [
            t.StructField("id", t.StringType(), False),
            t.StructField("name_first", t.StringType(), False),
            t.StructField("name_last", t.StringType(), False),
            t.StructField("male_flag", t.DoubleType(), True),
            t.StructField("attribution_status", t.IntegerType(), True),
        ]
    )

    patent_assignee = [
        ("6114900", "cf06cbad-b4f3-45f7-888a-c0d078f5b856", None),
        ("6114900", "cfdfdfcbad-b4f3-45f7-888a-c0d078f5b856", None),
    ]

    patent_assignee_schema = t.StructType(
        [
            t.StructField("patent_id", t.StringType(), False),
            t.StructField("assignee_id", t.StringType(), False),
            t.StructField("location_id", t.StringType(), True),
        ]
    )

    patent_inventor = [
        ("D419739", "fl:a._ln:george-1", "7674c183-cb8f-11eb-9615-121df0c29c1e"),
        ("D419739", "fl:a._ln:george-1-hjhj", "7674c183-cb8f-11eb-9615-121df0c29c1e"),
    ]

    patent_inventor_schema = t.StructType(
        [
            t.StructField("patent_id", t.StringType(), False),
            t.StructField("inventor_id", t.StringType(), False),
            t.StructField("location_id", t.StringType(), True),
        ]
    )
