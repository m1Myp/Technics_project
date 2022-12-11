import { Component, OnInit } from '@angular/core';
import { TestService } from "../test.service";
import {Info, InfoArray} from "../test-contracts";

@Component({
  selector: 'app-test-component',
  templateUrl: './testing.component.html',
  styleUrls: ['./testing.component.css']
})
export class TestingComponent implements OnInit {
  productData: InfoArray = [];

  constructor(private testService: TestService) { }

  ngOnInit(): void {
    this.getTest();
  }

  getTest() {
    this.testService.getTest().subscribe(
      {
        next: (data) => {
          console.log(data);
        },
        error: (error) => {
          console.log(error);
        }
      }
      );
  }

}
