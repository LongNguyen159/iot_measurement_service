import { Results } from "../usage-report/models/results";

export function groupDataByDevice(data: any[]) {
    const groupedData = data.reduce((accumulator, item) => {
        const deviceId = item.deviceId
        if (!accumulator[deviceId]) {
            accumulator[deviceId] = {
                name: `Device ${deviceId}`,
                type: 'line',
                data: [],
            }
        }
        accumulator[deviceId].data.push([item.timestamp, item.temperature])
        return accumulator
    }, {});
    console.log(groupedData)
    return groupedData
}