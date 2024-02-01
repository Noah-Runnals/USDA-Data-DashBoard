# file with used variables
comm_type = ['Total_Grains', 'Wheat', 'Course_Grains', 'Rice_Milled']
prod_type = ['Output', 'Total Supply', 'Trade', 'Total Use', 'Ending Stock']
time = ['2 Yr Actual', 'Last Yr Est.', "This Yr Projected"]
location = ['World', 'USA', 'Foreign']
# define nested dictionary to be filled out by extracted data
storage = \
    {"World": {
        'Total_Grains':
            {
                'Output': {'2 Yr Actual': [], 'Last Yr Est.': [], "This Yr Projected": []},
                'Total Supply': {'2 Yr Actual': [], 'Last Yr Est.': [], "This Yr Projected": []},
                'Trade': {'2 Yr Actual': [], 'Last Yr Est.': [], "This Yr Projected": []},
                'Total Use': {'2 Yr Actual': [], 'Last Yr Est.': [], "This Yr Projected": []},
                'Ending Stock': {'2 Yr Actual': [], 'Last Yr Est.': [], "This Yr Projected": []}

            }
        ,
        'Wheat':
            {
                'Output': {'2 Yr Actual': [], 'Last Yr Est.': [], "This Yr Projected": []},
                'Total Supply': {'2 Yr Actual': [], 'Last Yr Est.': [], "This Yr Projected": []},
                'Trade': {'2 Yr Actual': [], 'Last Yr Est.': [], "This Yr Projected": []},
                'Total Use': {'2 Yr Actual': [], 'Last Yr Est.': [], "This Yr Projected": []},
                'Ending Stock': {'2 Yr Actual': [], 'Last Yr Est.': [], "This Yr Projected": []}

            }
        ,
        'Course_Grains':
            {
                'Output': {'2 Yr Actual': [], 'Last Yr Est.': [], "This Yr Projected": []},
                'Total Supply': {'2 Yr Actual': [], 'Last Yr Est.': [], "This Yr Projected": []},
                'Trade': {'2 Yr Actual': [], 'Last Yr Est.': [], "This Yr Projected": []},
                'Total Use': {'2 Yr Actual': [], 'Last Yr Est.': [], "This Yr Projected": []},
                'Ending Stock': {'2 Yr Actual': [], 'Last Yr Est.': [], "This Yr Projected": []}

            }
        ,
        'Rice_Milled':
            {
                'Output': {'2 Yr Actual': [], 'Last Yr Est.': [], "This Yr Projected": []},
                # add tuple to this: (date of file read, data number)
                'Total Supply': {'2 Yr Actual': [], 'Last Yr Est.': [], "This Yr Projected": []},
                'Trade': {'2 Yr Actual': [], 'Last Yr Est.': [], "This Yr Projected": []},
                'Total Use': {'2 Yr Actual': [], 'Last Yr Est.': [], "This Yr Projected": []},
                'Ending Stock': {'2 Yr Actual': [], 'Last Yr Est.': [], "This Yr Projected": []}

            }

    }, "USA": {
        'Total_Grains':
            {
                'Output': {'2 Yr Actual': [], 'Last Yr Est.': [], "This Yr Projected": []},
                'Total Supply': {'2 Yr Actual': [], 'Last Yr Est.': [], "This Yr Projected": []},
                'Trade': {'2 Yr Actual': [], 'Last Yr Est.': [], "This Yr Projected": []},
                'Total Use': {'2 Yr Actual': [], 'Last Yr Est.': [], "This Yr Projected": []},
                'Ending Stock': {'2 Yr Actual': [], 'Last Yr Est.': [], "This Yr Projected": []}

            }
        ,
        'Wheat':
            {
                'Output': {'2 Yr Actual': [], 'Last Yr Est.': [], "This Yr Projected": []},
                'Total Supply': {'2 Yr Actual': [], 'Last Yr Est.': [], "This Yr Projected": []},
                'Trade': {'2 Yr Actual': [], 'Last Yr Est.': [], "This Yr Projected": []},
                'Total Use': {'2 Yr Actual': [], 'Last Yr Est.': [], "This Yr Projected": []},
                'Ending Stock': {'2 Yr Actual': [], 'Last Yr Est.': [], "This Yr Projected": []}

            }
        ,
        'Course_Grains':
            {
                'Output': {'2 Yr Actual': [], 'Last Yr Est.': [], "This Yr Projected": []},
                'Total Supply': {'2 Yr Actual': [], 'Last Yr Est.': [], "This Yr Projected": []},
                'Trade': {'2 Yr Actual': [], 'Last Yr Est.': [], "This Yr Projected": []},
                'Total Use': {'2 Yr Actual': [], 'Last Yr Est.': [], "This Yr Projected": []},
                'Ending Stock': {'2 Yr Actual': [], 'Last Yr Est.': [], "This Yr Projected": []}

            }
        ,
        'Rice_Milled':
            {
                'Output': {'2 Yr Actual': [], 'Last Yr Est.': [], "This Yr Projected": []},
                'Total Supply': {'2 Yr Actual': [], 'Last Yr Est.': [], "This Yr Projected": []},
                'Trade': {'2 Yr Actual': [], 'Last Yr Est.': [], "This Yr Projected": []},
                'Total Use': {'2 Yr Actual': [], 'Last Yr Est.': [], "This Yr Projected": []},
                'Ending Stock': {'2 Yr Actual': [], 'Last Yr Est.': [], "This Yr Projected": []}

            }

    }, "Foreign": {
        'Total_Grains':
            {
                'Output': {'2 Yr Actual': [], 'Last Yr Est.': [], "This Yr Projected": []},
                'Total Supply': {'2 Yr Actual': [], 'Last Yr Est.': [], "This Yr Projected": []},
                'Trade': {'2 Yr Actual': [], 'Last Yr Est.': [], "This Yr Projected": []},
                'Total Use': {'2 Yr Actual': [], 'Last Yr Est.': [], "This Yr Projected": []},
                'Ending Stock': {'2 Yr Actual': [], 'Last Yr Est.': [], "This Yr Projected": []}

            }
        ,
        'Wheat':
            {
                'Output': {'2 Yr Actual': [], 'Last Yr Est.': [], "This Yr Projected": []},
                'Total Supply': {'2 Yr Actual': [], 'Last Yr Est.': [], "This Yr Projected": []},
                'Trade': {'2 Yr Actual': [], 'Last Yr Est.': [], "This Yr Projected": []},
                'Total Use': {'2 Yr Actual': [], 'Last Yr Est.': [], "This Yr Projected": []},
                'Ending Stock': {'2 Yr Actual': [], 'Last Yr Est.': [], "This Yr Projected": []}

            }
        ,
        'Course_Grains':
            {
                'Output': {'2 Yr Actual': [], 'Last Yr Est.': [], "This Yr Projected": []},
                'Total Supply': {'2 Yr Actual': [], 'Last Yr Est.': [], "This Yr Projected": []},
                'Trade': {'2 Yr Actual': [], 'Last Yr Est.': [], "This Yr Projected": []},
                'Total Use': {'2 Yr Actual': [], 'Last Yr Est.': [], "This Yr Projected": []},
                'Ending Stock': {'2 Yr Actual': [], 'Last Yr Est.': [], "This Yr Projected": []}

            }
        ,
        'Rice_Milled':
            {
                'Output': {'2 Yr Actual': [], 'Last Yr Est.': [], "This Yr Projected": []},
                'Total Supply': {'2 Yr Actual': [], 'Last Yr Est.': [], "This Yr Projected": []},
                'Trade': {'2 Yr Actual': [], 'Last Yr Est.': [], "This Yr Projected": []},
                'Total Use': {'2 Yr Actual': [], 'Last Yr Est.': [], "This Yr Projected": []},
                'Ending Stock': {'2 Yr Actual': [], 'Last Yr Est.': [], "This Yr Projected": []}

            }

    }
    }