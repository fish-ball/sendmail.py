#!/usr/bin/env php
<?php
mail(
'57082212@qq.com',   
"=?UTF-8?B?".base64_encode("你好")."?=",
'This is a test mail 你好',
"Content-type: text/plain; charset=utf-8;\n");
//From: Shenzhen JP <szshouko-fm@sz-nicchu.com>\n

