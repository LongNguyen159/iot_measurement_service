import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PiePlotComponent } from './pie-plot.component';

describe('PiePlotComponent', () => {
  let component: PiePlotComponent;
  let fixture: ComponentFixture<PiePlotComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [PiePlotComponent]
    });
    fixture = TestBed.createComponent(PiePlotComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
