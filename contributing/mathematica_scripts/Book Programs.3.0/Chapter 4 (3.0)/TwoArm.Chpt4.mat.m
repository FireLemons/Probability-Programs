(***********************************************************************
This file was generated automatically by the Mathematica front end.
It contains Initialization cells from a Notebook file, which typically
will have the same name as this file except ending in ".nb" instead of
".m".

This file is intended to be loaded into the Mathematica kernel using
the package loading commands Get or Needs.  Doing so is equivalent to
using the Evaluate Initialiation Cells menu command in the front end.

DO NOT EDIT THIS FILE.  This entire file is regenerated automatically 
each time the parent Notebook file is saved in the Mathematica front end.
Any changes you make to this file will be overwritten.
***********************************************************************)

Clear[TwoArm];
TwoArm[n_, x_, y_, s_, print_] :=
Block[{win1 = 0, lose1 = 0, win2 = 0, lose2 = 0,
       p1, p2,
       currentmachine = 1,
       machinelist = {},
       resultlist = {}
      },
      If[(s == 1),
      
(* Play-the-better-machine strategy *)

      Block[{},
            For[i = 1, i <= n, i++,
                machinelist = 
                     Append[machinelist,
                            currentmachine
                           ];
                If[(currentmachine == 1),
                Block[{},
                      If[(Random[] < x),
                      Block[{},
                            win1++;
                            resultlist = 
                                    Append[resultlist,
                                           "W"
                                          ]
                           ],
                      Block[{},
                            lose1++;
                            resultlist =
                                    Append[resultlist,
                                           "L"
                                          ]
                           ] 
                        ]
                     ],
                Block[{},
                      If[(Random[] < y),
                      Block[{},
                            win2++;
                            resultlist =
                                    Append[resultlist,
                                           "W"
                                          ]
                           ], 
                      Block[{},
                            lose2++;
                            resultlist =
                                    Append[resultlist,
                                           "L"
                                          ]
                           ] 
                        ]
                     ]
                   ];   (* endif *)
                p1 = (win1 + 1)/(win1 + lose1 + 2);
                p2 = (win2 + 1)/(win2 + lose2 + 2);
                If[(p1 > p2),
                   currentmachine = 1,
                   currentmachine = 2
                  ]
                ]  (* endfor *)
            ],  (* endblock *)
            
 (* Play-the-winner-strategy *)          
           
      Block[{},
            For[i = 1, i <= n, i++,
                machinelist = 
                     Append[machinelist,
                            currentmachine
                           ];
                If[(currentmachine == 1),
                Block[{},
                      If[(Random[] < x),
                      Block[{},
                            win1++;
                            resultlist = 
                                    Append[resultlist,
                                           "W"
                                          ]
                           ],
                      Block[{},
                            lose1++;
                            resultlist =
                                    Append[resultlist,
                                           "L"
                                          ];
                            currentmachine = 2
                           ]
                        ]
                     ],
                Block[{},
                      If[(Random[] < y),
                      Block[{},
                            win2++;
                            resultlist = 
                                    Append[resultlist,
                                           "W"
                                          ]
                           ],
                      Block[{},
                            lose2++;
                            resultlist =
                                    Append[resultlist,
                                           "L"
                                          ];
                            currentmachine = 1
                           ]
                        ]
                     ]
                   ]  (* endif *)
                ]  (* endfor *)
            ]  (* endblock *)
        ];  (* end big if *)
      If[print,
         Print["Machine  Result"]
        ];
      If[print,
         For[i = 1, i <= n, i++, 
             Print["   ",
                   machinelist[[i]],
                   "       ",
                   resultlist[[i]]
                  ]
            ]
        ];
      Show[Plot[BetaDensity[win1 + 1, lose1 + 1, z],
                {z, 0, 1},
                DisplayFunction -> Identity
               ],
           Plot[BetaDensity[win2 + 1, lose2 + 1, z],
                {z, 0, 1},
                PlotStyle -> {{Dashing[{0.02, 0.02}]}},
                DisplayFunction -> Identity
               ],
           DisplayFunction -> $DisplayFunction,
           PlotRange -> All
          ]
    ]
