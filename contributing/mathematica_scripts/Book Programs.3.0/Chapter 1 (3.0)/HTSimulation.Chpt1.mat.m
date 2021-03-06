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

Clear[HTSimulation];
HTSimulation[n_, m_, print_] :=
Block[{winningslist = {},
       timesinleadlist = {},
       currentwinnings,
       previouscurrentwinnings,
       tosslist = {{0, 0}}
      },
      For[i = 1, i <= n, i++,
          currentwinnings = 0;
          previouswinnings = 0;
          lead = 0;
          For[j = 1, j <= m, j++,
              If[(Random[] < .5),
                 currentwinnings++,
                 currentwinnings--
                ];
              If[((n == 1)&&(print)),
                 tosslist =
                   Append[tosslist, 
                          {j, currentwinnings}]
                ];
              If[((currentwinnings > 0)||
                  ((currentwinnings == 0)&&
                  (previouswinnings > 0))
                 ),
                 lead++;
                ];
              previouswinnings = currentwinnings;
             ];
          winningslist =
            Append[winningslist, currentwinnings];
          timesinleadlist = 
            Append[timesinleadlist, lead];
         ];
      If[((n == 1)&&(print)),
         ListPlot[tosslist, 
                  PlotJoined -> True,
                  AxesOrigin -> {0, 0}
                 ],
         If[print,
            Print["The first spike graph below shows the"];
            Print["distribution of winnings.  The second"];
            Print["spike graph shows the distribution of"];
            Print["the number of times in the lead."];
            Spikegraph[SpikeData[winningslist], 
                       Min[winningslist],
                       Max[winningslist],
                       True
                      ];
            Spikegraph[SpikeData[timesinleadlist],
                       Min[timesinleadlist],
                       Max[timesinleadlist],
                       True
                      ]
           ]
        ];
      Return[{winningslist, timesinleadlist}]
     ]