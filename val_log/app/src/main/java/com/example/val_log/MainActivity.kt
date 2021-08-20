package com.example.val_log

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.util.Log

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)


        Log.e("MainActivity","testlog")//오류
        Log.w("MainActivity","testlog")//경고
        Log.i("MainActivity","testlog")//정보
        Log.d("MainActivity","testlog")//디버
        Log.v("MainActivity","testlog")//상세

        //var => 바꾸기 가능 , val => 상수 못바꿈.
        var value = "여기는 values입니다."
        val value2 = "여기는 value2입니다"


        value = "여기는 value가 아닙니다~!~!"
    }
}