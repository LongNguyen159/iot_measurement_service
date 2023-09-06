import { Results } from "../usage-report/models/results";

export function groupDataByDevice(data: any[]) {
    const groupedData = data.reduce((accumulator, item) => {
        const deviceId = item.deviceId
        if (!accumulator[deviceId]) {
            accumulator[deviceId] = {
                data: [],
            }
        }
        accumulator[deviceId].data.push([item.timestamp, item.temperature])
        return accumulator
    }, {});
    console.log(groupedData)
    return groupedData
}

// export function processGroupDataIntoSeriesData(groupedData: any) {
//     const seriesData = Object.values(groupedData).map((item: any) => {
//         name: item.name,
//         type: item.type,
//         data: item.data.map(([time: string, temperature])=> {

//         })
//     })
// }