import { Component, OnInit, OnDestroy } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { UsageReportService } from '../../services/usage-report.service';
import { EChartsOption } from 'echarts';
import { Subscription } from 'rxjs';
import { Results } from '../../models/results';

@Component({
  selector: 'app-line-plot',
  templateUrl: './line-plot.component.html',
  styleUrls: ['./line-plot.component.scss']
})
export class LinePlotComponent implements OnInit, OnDestroy {
  chartOption!: EChartsOption;
  year: number = 1950
  count: number = 0

  constructor(private http: HttpClient, private usageReportService: UsageReportService) {}

  ngOnInit(): void {
    this.updateChart()
    this.simulateDynamicData()
  }

  simulateDynamicData() {
    // if (this.count < 69) {
    //   setTimeout(()=> {
    //     this.year = this.year + 1;
    //     this.updateChart()
    //     this.count++
    //     this.simulateDynamicData()
    //   },2000)
    // }
  }

  updateChart(): void {
    this.usageReportService.getDailyResults('2023-09-06').subscribe((data: Results[]) => {
      
    })


    // this.usageReportService.getYearlyResults(this.year).subscribe(data => {
    //   this.chartOption = {
    //     title: {
    //       text: `Results ${this.year}`
    //     },
    //     xAxis: {
    //       type: 'category',
    //       data: data.xAxisData
    //     },
    //     yAxis: {
    //       type: 'value'
    //     },
    //     legend: {
    //       type: 'scroll',
    //       show: true,
    //       width: 50,
    //       orient: 'vertical',
    //       padding: 10,
    //       bottom:0,
    //       right: 0
    //     },
    //     series: data.seriesData
    //   };
    // });
  }
  
  ngOnDestroy(): void {
  }
}
