/**
 * Jordan PG Grade Map — Configuration
 * 
 * Edit this file to update the map source or the PG adjustment table
 * without modifying the HTML or JavaScript code.
 * 
 * Badge styles:
 *   "70" = orange (PG 70 zone color)
 *   "64" = blue  (PG 64 zone color)
 */
window.PG_CONFIG = {

    // Map iframe source file
    mapSource: "Jordan-PG-Grade-Map-98_valid.html",

    // PG Adjustment Table
    adjustmentTable: {

        // Column headers for each zone (in order)
        zones: [
            {
                id: "zone-70",
                label: { en: "PG 70 -10 Zone", ar: "منطقة PG 70 -10" },
                headerStyle: "70"
            },
            {
                id: "zone-64",
                label: { en: "PG 64 -10 Zone", ar: "منطقة PG 64 -10" },
                headerStyle: "64"
            }
        ],

        // Table rows — each row has a traffic condition and a grade per zone
        rows: [
            {
                condition: {
                    lines: [
                        { en: "Speed ≥ 70 km/h", ar: "السرعة ≥ 70 كم/س" },
                        { en: "Traffic < 10m ESAL", ar: "حركة المرور < 10 مليون ESAL" }
                    ],
                    connector: { en: "AND", ar: "و" }
                },
                grades: [
                    { label: "PG 70 -10", style: "70" },
                    { label: "PG 64 -10", style: "64" }
                ]
            },
            {
                condition: {
                    lines: [
                        { en: "20 ≤ Speed < 70 km/h", ar: "20 ≤ السرعة < 70 كم/س" },
                        { en: "10m ≤ Traffic < 30m ESAL", ar: "10 مليون ≤ حركة المرور < 30 مليون ESAL" }
                    ],
                    connector: { en: "OR", ar: "أو" }
                },
                grades: [
                    { label: "PG 76 -10", style: "70" },
                    { label: "PG 70 -10", style: "70" }
                ]
            },
            {
                condition: {
                    lines: [
                        { en: "Speed < 20 km/h", ar: "السرعة < 20 كم/س" },
                        { en: "Traffic ≥ 30m ESAL", ar: "حركة المرور ≥ 30 مليون ESAL" }
                    ],
                    connector: { en: "OR", ar: "أو" }
                },
                grades: [
                    { label: "PG 82 -10", style: "70" },
                    { label: "PG 76 -10", style: "70" }
                ]
            }
        ]
    }
};
