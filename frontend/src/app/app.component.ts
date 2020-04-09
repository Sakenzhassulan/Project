import {Component, OnInit} from '@angular/core';
import {LazyLoadScriptService} from './lazy-load-script.service';
import {scripts} from './scripts';

declare var $;

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  title = 'Ocenika';


  constructor(private lazyLoadService: LazyLoadScriptService) {
  }

  ngOnInit() {
    for (const scriptUrl of scripts) {
      this.lazyLoadService.loadScript(scriptUrl);
    }
  }


}
