<?php
/**
 * Created by PhpStorm.
 * User: lilizhao
 * Date: 2017/5/3
 * Time: 11:41
 */
if($_POST){
    $arr = array(
        'res' => 1,
        'msg' => $_POST
    );
    echo json_encode($arr);
}else{
    $arr = array(
        'res' => -1,
        'msg' => "没有post数据"
    );
    echo json_encode($arr);
}