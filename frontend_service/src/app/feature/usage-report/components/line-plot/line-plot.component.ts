import { Component, OnInit, OnDestroy, Input, OnChanges, SimpleChanges } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { UsageReportService } from '../../services/usage-report.service';
import { EChartsOption } from 'echarts';
import { Subscription } from 'rxjs';
import { Results } from '../../models/results';
import * as echarts from 'echarts'

@Component({
  selector: 'app-line-plot',
  templateUrl: './line-plot.component.html',
  styleUrls: ['./line-plot.component.scss']
})
export class LinePlotComponent implements OnInit, OnDestroy, OnChanges {
  chartOption: EChartsOption;

  @Input() plotData: any

  constructor(private http: HttpClient, private usageReportService: UsageReportService) {}

  ngOnInit(): void {
  }

  ngOnChanges(changes: SimpleChanges): void {
    if (changes.plotData && changes.plotData.currentValue !== undefined) {
      this.updateChart()
    }
  }

  updateChart(): void {
    const series: echarts.SeriesOption[] = Object.keys(this.plotData).map(item => ({
      name: `Device ${item}`,
      type: 'line',
      data: this.plotData[item].data.map(([time, temp]: [string, number]) => ([
        new Date(time),
        temp,
      ])),
    }));

    console.log('from plot component:', this.plotData)
    console.log(series)

    this.chartOption = {
      title: {
        text: 'Daily Temperature',
      },
      xAxis: {
        type: 'time',
        name: 'Time',
        nameLocation: 'middle',
        nameGap: 50,
      },
      yAxis: {
        type: 'value',
        name: 'Temperature (°C)',
        nameLocation: 'middle',
        nameGap: 50,
      },
      legend: {
        show: true
      },
      series: series
    }
  }
  
  ngOnDestroy(): void {
  }
}
