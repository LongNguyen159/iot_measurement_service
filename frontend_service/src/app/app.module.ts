import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { LinePlotComponent } from './feature/usage-report/components/line-plot/line-plot.component';
import { HttpClientModule } from  '@angular/common/http';
import { NgxEchartsModule } from 'ngx-echarts';
import { PiePlotComponent } from './feature/usage-report/components/pie-plot/pie-plot.component';

@NgModule({
  declarations: [
    AppComponent,
    LinePlotComponent,
    PiePlotComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    NgxEchartsModule.forRoot({
      echarts: () => import('echarts')
    }),
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
