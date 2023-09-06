import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { LinePlotComponent } from './feature/usage-report/components/line-plot/line-plot.component';
import { HttpClientModule } from  '@angular/common/http';
import { NgxEchartsModule } from 'ngx-echarts';
import { PiePlotComponent } from './feature/usage-report/components/pie-plot/pie-plot.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { MatButtonModule } from '@angular/material/button';
import { UsageReportPageComponent } from './pages/usage-report-page/usage-report-page.component';
import { HomepageComponent } from './pages/homepage/homepage.component';
@NgModule({
  declarations: [
    AppComponent,
    LinePlotComponent,
    PiePlotComponent,
    UsageReportPageComponent,
    HomepageComponent,
  ],
  imports: [
    MatButtonModule,
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    NgxEchartsModule.forRoot({
      echarts: () => import('echarts')
    }),
    BrowserAnimationsModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
